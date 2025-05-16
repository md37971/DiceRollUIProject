import java.io.*;
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Michael Delgado
 * Github: github.com/md37971
 * Developed using Apache NetBeans's IDE.
 */
public class LoginCheck{
    private String username = "GUEST_USER";
    private String password = "";
    public boolean isLoggedIn = false;
    
    public LoginCheck() {
        this.username = "GUEST_USER";
        this.password = "";
    }
    
    public LoginCheck(String username, String password){
        this.username = username;
        this.password = password;
        loginCheck();
    }
    
    public void setusername(String username) {
        this.username = username;
    }
    
    public void setPassword(String password) {
        this.password = password;
    }
    
    public String getusername() {
        return username;
    }
    
    private String getPassword() {
        return password;
    }
    
    public void loginCheck() {
        try {
            BufferedReader br = new BufferedReader(new FileReader("src//logininfo//loginCredentials.txt"));
            String inline = "";
            while((inline = br.readLine()) != null) {
                String[] token = inline.split(":");
                if(this.username.equals(token[0]) && this.password.equals(token[1])) {
                    System.out.println("SUCESSFUL LOGIN");
                    this.isLoggedIn = true;
                    return;
                }
            }
            this.isLoggedIn = false;
        }catch(IOException e1) {
            System.out.println("File Not Found" + e1);
            this.isLoggedIn = false;
        }
    }
}
