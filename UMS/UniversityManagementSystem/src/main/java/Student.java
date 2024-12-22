import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class Student extends User {
    private String major;
    private int year;
    private double gpa;
    private List<Course> courses = new ArrayList<>();
    private ResearchProject diplomaProject;
    private List<Book> borrowedBooks = new ArrayList<>();

    public Student(String id, String name, String email, String password, String role, String major, int year, double gpa) {
        super(id, name, email, password, role);
        this.major = major;
        this.year = year;
        this.gpa = gpa;
    }

    public void registerForCourse(Course course) {
        if (!courses.contains(course)) {
            courses.add(course);
            System.out.println("Successfully registered for course: " + course.getName());
        } else {
            System.out.println("Already registered for this course.");
        }
    }

    public List<Mark> viewTranscript() {
        // Placeholder: Retrieve marks from a database or system
        return new ArrayList<>();
    }

    public void rateTeacher(Teacher teacher, int rating) {
        System.out.println("Rated teacher " + teacher.getName() + " with " + rating + " stars.");
    }

    public void borrowBook(Librarian librarian, Book book) {
        String checkAvailabilityQuery = "SELECT * FROM books WHERE isbn = ? AND is_available = TRUE";
        String borrowBookQuery = "INSERT INTO borrowed_books (book_id, user_id) VALUES (?, ?)";
        String updateBookAvailabilityQuery = "UPDATE books SET is_available = FALSE WHERE isbn = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement checkStmt = connection.prepareStatement(checkAvailabilityQuery)) {

            checkStmt.setString(1, book.getIsbn());
            ResultSet rs = checkStmt.executeQuery();

            if (rs.next()) {
                int bookId = rs.getInt("id");

                try (PreparedStatement borrowStmt = connection.prepareStatement(borrowBookQuery);
                     PreparedStatement updateStmt = connection.prepareStatement(updateBookAvailabilityQuery)) {

                    connection.setAutoCommit(false);

                    borrowStmt.setInt(1, bookId);
                    borrowStmt.setString(2, this.id);
                    borrowStmt.executeUpdate();

                    updateStmt.setString(1, book.getIsbn());
                    updateStmt.executeUpdate();

                    connection.commit();
                    borrowedBooks.add(book);
                    System.out.println("Book borrowed successfully.");
                } catch (Exception e) {
                    connection.rollback();
                    System.out.println("Error borrowing book. Transaction rolled back.");
                    e.printStackTrace();
                } finally {
                    connection.setAutoCommit(true);
                }
            } else {
                System.out.println("Book is not available.");
            }
        } catch (Exception e) {
            System.out.println("Failed to borrow book.");
            e.printStackTrace();
        }
    }

    public void returnBook(Librarian librarian, Book book) {
        String findBorrowedBookQuery = "SELECT bb.id FROM borrowed_books bb " +
                "JOIN books b ON bb.book_id = b.id " +
                "WHERE b.isbn = ? AND bb.user_id = ? AND bb.return_date IS NULL";
        String updateBorrowedBookQuery = "UPDATE borrowed_books SET return_date = CURRENT_TIMESTAMP WHERE id = ?";
        String updateBookAvailabilityQuery = "UPDATE books SET is_available = TRUE WHERE isbn = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement findStmt = connection.prepareStatement(findBorrowedBookQuery)) {

            findStmt.setString(1, book.getIsbn());
            findStmt.setString(2, this.id);
            ResultSet rs = findStmt.executeQuery();

            if (rs.next()) {
                int borrowedBookId = rs.getInt("id");

                try (PreparedStatement updateBorrowStmt = connection.prepareStatement(updateBorrowedBookQuery);
                     PreparedStatement updateBookStmt = connection.prepareStatement(updateBookAvailabilityQuery)) {

                    connection.setAutoCommit(false);

                    updateBorrowStmt.setInt(1, borrowedBookId);
                    updateBorrowStmt.executeUpdate();

                    updateBookStmt.setString(1, book.getIsbn());
                    updateBookStmt.executeUpdate();

                    connection.commit();
                    borrowedBooks.remove(book);
                    System.out.println("Book returned successfully.");
                } catch (Exception e) {
                    connection.rollback();
                    System.out.println("Error returning book. Transaction rolled back.");
                    e.printStackTrace();
                } finally {
                    connection.setAutoCommit(true);
                }
            } else {
                System.out.println("No record found for this book.");
            }
        } catch (Exception e) {
            System.out.println("Failed to return book.");
            e.printStackTrace();
        }
    }

    public boolean canGraduate() {
        return year >= 4 && gpa >= 2.0;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public double getGpa() {
        return gpa;
    }

    public void setGpa(double gpa) {
        this.gpa = gpa;
    }

    public List<Course> getCourses() {
        return courses;
    }

    public ResearchProject getDiplomaProject() {
        return diplomaProject;
    }

    public void setDiplomaProject(ResearchProject diplomaProject) {
        this.diplomaProject = diplomaProject;
    }

    public List<Book> getBorrowedBooks() {
        return borrowedBooks;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", major='" + major + '\'' +
                ", year=" + year +
                ", gpa=" + gpa +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Student student = (Student) obj;
        return id.equals(student.id);
    }

    @Override
    public int hashCode() {
        return id.hashCode();
    }
}
