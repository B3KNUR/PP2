import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class Teacher {

    private int id;
    private String name;
    private TeacherType teacherType;
    private String schedule;
    private String researchField;

    public Teacher(int id, String name, TeacherType teacherType, String schedule, String researchField) {
        this.id = id;
        this.name = name;
        this.teacherType = teacherType;
        this.schedule = schedule;
        this.researchField = researchField;
    }

    public List<Course> viewCourses() {
        List<Course> courses = new ArrayList<>();
        String query = "SELECT * FROM courses WHERE teacher_id = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setInt(1, this.id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                Course course = new Course(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getInt("credits")
                );
                courses.add(course);
            }

        } catch (Exception e) {
            System.out.println("Failed to retrieve courses.");
            e.printStackTrace();
        }

        return courses;
    }

    public void assignMark(Student student, int courseId, int mark) {
        String query = "INSERT INTO marks (student_id, course_id, mark) VALUES (?, ?, ?)";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setInt(1, student.getId());
            pstmt.setInt(2, courseId);
            pstmt.setInt(3, mark);
            pstmt.executeUpdate();
            System.out.println("Mark assigned successfully.");

        } catch (Exception e) {
            System.out.println("Failed to assign mark.");
            e.printStackTrace();
        }
    }

    public void sendComplaint(Student student, String urgencyLevel, String complaint) {
        String query = "INSERT INTO complaints (student_id, teacher_id, urgency_level, complaint) VALUES (?, ?, ?, ?)";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setInt(1, student.getId());
            pstmt.setInt(2, this.id);
            pstmt.setString(3, urgencyLevel);
            pstmt.setString(4, complaint);
            pstmt.executeUpdate();
            System.out.println("Complaint sent successfully.");

        } catch (Exception e) {
            System.out.println("Failed to send complaint.");
            e.printStackTrace();
        }
    }

    public List<Student> viewStudents() {
        List<Student> students = new ArrayList<>();
        String query = "SELECT s.id, s.name FROM students s JOIN enrollments e ON s.id = e.student_id WHERE e.course_id IN (SELECT id FROM courses WHERE teacher_id = ?)";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setInt(1, this.id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                Student student = new Student(
                        rs.getInt("id"),
                        rs.getString("name")
                        rs.getString("email")
                        rs.getString("password")
                        rs.getString("role")
                );
                students.add(student);
            }

        } catch (Exception e) {
            System.out.println("Failed to retrieve students.");
            e.printStackTrace();
        }

        return students;
    }

    public void writeRecommendationLetter(Student student) {
        String letter = "To Whom It May Concern,\n\n" +
                "I am writing to highly recommend " + student.getName() + " for your program. " +
                "They have demonstrated exceptional skills and dedication during their studies.\n\n" +
                "Sincerely,\n" + this.name;

        System.out.println("Recommendation Letter:\n" + letter);
    }

    public void conductResearch() {
        System.out.println("Conducting research in the field of " + this.researchField);
    }

    public void publishResearchPaper(String paperTitle) {
        String query = "INSERT INTO research_papers (teacher_id, title) VALUES (?, ?)";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setInt(1, this.id);
            pstmt.setString(2, paperTitle);
            pstmt.executeUpdate();
            System.out.println("Research paper published successfully.");

        } catch (Exception e) {
            System.out.println("Failed to publish research paper.");
            e.printStackTrace();
        }
    }

    public int calculateHIndex() {
        String query = "SELECT COUNT(*) AS citations FROM research_papers WHERE teacher_id = ?";
        int hIndex = 0;

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setInt(1, this.id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                hIndex = rs.getInt("citations");
            }

        } catch (Exception e) {
            System.out.println("Failed to calculate H-Index.");
            e.printStackTrace();
        }

        return hIndex;
    }

    public void addCourse(Course course) {
        String query = "INSERT INTO courses (name, credits, teacher_id) VALUES (?, ?, ?)";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setString(1, course.getCourseName());
            pstmt.setInt(2, course.getCredits());
            pstmt.setInt(3, this.id);
            pstmt.executeUpdate();
            System.out.println("Course added successfully.");

        } catch (Exception e) {
            System.out.println("Failed to add course.");
            e.printStackTrace();
        }
    }

    public void manageCourse(int courseId, String newName, int newCredits) {
        String query = "UPDATE courses SET name = ?, credits = ? WHERE id = ? AND teacher_id = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setString(1, newName);
            pstmt.setInt(2, newCredits);
            pstmt.setInt(3, courseId);
            pstmt.setInt(4, this.id);
            pstmt.executeUpdate();
            System.out.println("Course updated successfully.");

        } catch (Exception e) {
            System.out.println("Failed to manage course.");
            e.printStackTrace();
        }
    }

    public List<String> viewRequests() {
        List<String> requests = new ArrayList<>();
        String query = "SELECT request FROM course_requests WHERE teacher_id = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(query)) {

            pstmt.setInt(1, this.id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                requests.add(rs.getString("request"));
            }

        } catch (Exception e) {
            System.out.println("Failed to retrieve course requests.");
            e.printStackTrace();
        }

        return requests;
    }

    public TeacherType getTeacherType() {
        return teacherType;
    }

    public void setTeacherType(TeacherType teacherType) {
        this.teacherType = teacherType;
    }

    public String getSchedule() {
        return schedule;
    }

    public void setSchedule(String schedule) {
        this.schedule = schedule;
    }

    public String getResearchField() {
        return researchField;
    }

    public void setResearchField(String researchField) {
        this.researchField = researchField;
    }

    @Override
    public String toString() {
        return "Teacher{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", teacherType=" + teacherType +
                ", schedule='" + schedule + '\'' +
                ", researchField='" + researchField + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Teacher teacher = (Teacher) o;

        return id == teacher.id;
    }

    @Override
    public int hashCode() {
        return id;
    }
}
