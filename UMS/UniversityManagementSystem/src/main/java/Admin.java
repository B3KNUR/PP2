import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class Admin extends User {

    public Admin(String id, String name, String email, String password, String role) {
        super(id, name, email, password, role);
    }

    public void addUser(List<User> users) {
        String insertQuery = "INSERT INTO users (username, password, role) VALUES (?, ?, ?)";

        try (Connection connection = DBConnection.getConnection()) {
            connection.setAutoCommit(false);

            try (PreparedStatement pstmt = connection.prepareStatement(insertQuery)) {
                for (User user : users) {
                    pstmt.setString(1, user.getName());
                    pstmt.setString(2, user.getPassword());
                    pstmt.setString(3, user.getRole());
                    pstmt.addBatch();
                }

                pstmt.executeBatch();
                connection.commit();
                System.out.println("Users added successfully.");
            } catch (Exception e) {
                connection.rollback(); // Rollback the transaction on error
                System.out.println("Error adding users. Transaction rolled back.");
                e.printStackTrace();
            } finally {
                connection.setAutoCommit(true);
            }
        } catch (Exception e) {
            System.out.println("Failed to add users.");
            e.printStackTrace();
        }
    }

    // Method to remove a user from the database by username
    public void removeUser(User user) {
        String deleteQuery = "DELETE FROM users WHERE username = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(deleteQuery)) {

            pstmt.setString(1, user.getName());
            int affectedRows = pstmt.executeUpdate();

            if (affectedRows > 0) {
                System.out.println("User " + user.getName() + " removed successfully.");
            } else {
                System.out.println("User " + user.getName() + " not found.");
            }

        } catch (Exception e) {
            System.out.println("Failed to remove user.");
            e.printStackTrace();
        }
    }

    public List<User> getUsers() {
        List<User> users = new ArrayList<>();
        String selectQuery = "SELECT * FROM users";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(selectQuery);
             ResultSet rs = pstmt.executeQuery()) {

            while (rs.next()) {
                User user = new User(
                        rs.getString("id"),
                        rs.getString("name"),
                        rs.getString("email"),
                        rs.getString("password"),
                        rs.getString("role")
                );
                users.add(user);
            }

        } catch (Exception e) {
            System.out.println("Failed to retrieve users.");
            e.printStackTrace();
        }

        return users;
    }

    public void updateUser(User updatedUser) {
        String updateQuery = "UPDATE users SET username = ?, email = ?, password = ?, role = ? WHERE id = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(updateQuery)) {

            pstmt.setString(1, updatedUser.getName());
            pstmt.setString(2, updatedUser.getEmail());
            pstmt.setString(3, updatedUser.getPassword());
            pstmt.setString(4, updatedUser.getRole());
            pstmt.setString(5, updatedUser.getId());

            int affectedRows = pstmt.executeUpdate();
            if (affectedRows > 0) {
                System.out.println("User " + updatedUser.getName() + " updated successfully.");
            } else {
                System.out.println("User not found.");
            }

        } catch (Exception e) {
            System.out.println("Failed to update user.");
            e.printStackTrace();
        }
    }

    public void resetPassword(User user, String newPassword) {
        String updateQuery = "UPDATE users SET password = ? WHERE id = ?";

        try (Connection connection = DBConnection.getConnection();
             PreparedStatement pstmt = connection.prepareStatement(updateQuery)) {

            pstmt.setString(1, newPassword);
            pstmt.setString(2, user.getId());

            int affectedRows = pstmt.executeUpdate();
            if (affectedRows > 0) {
                System.out.println("Password for user " + user.getName() + " has been reset.");
            } else {
                System.out.println("User not found.");
            }

        } catch (Exception e) {
            System.out.println("Failed to reset password.");
            e.printStackTrace();
        }
    }
}
