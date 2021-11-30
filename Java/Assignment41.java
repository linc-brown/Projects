import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.*;


/**
 * Lincoln Brown
 * Assignment 4.1
 * CIS404-308A
 * Professor Payne
 * 
 * 
 */
@WebServlet(urlPatterns = {"/Assignment41"})
public class Assignment31 extends HttpServlet {
    static java.nio.charset.Charset myCharset = java.nio.charset.Charset.forName("US-ASCII");
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        
        java.io.PrintWriter out = response.getWriter();
        
        try{
           String output = readWriteFile("C:\\Temp\\servlet1.dat");
            out.println(output);
        }
        catch(Exception e){
            
        }
    }
    
    public String startWrap(String title){
        String openTitle = "<html>\n<head>\n<title>\n";
        String closeTitle = title + "</title></head>";
        String body = "<body>\n<div>\n";
        String wrapped = openTitle + closeTitle + body;        
        return wrapped;
    }
    
    public String endWrap(){
        String close = "</div></body></html>";
        return close;
    }
    public String readWriteFile(String fileName){
        StringBuilder output = new StringBuilder("");
        
        Path target = Paths.get(fileName);
        try{
            java.util.List<String> lines = null;
            lines = Files.readAllLines(target, myCharset);
            
            if (lines != null){
                for(String line : lines){
                    output.append(startWrap("Servlet1"));
                    output.append(line).append("<br />\n");
                    output.append(endWrap());
                }
            }
            
            
        } catch (IOException ex) {
            output.append("File not found");
        }
        return output.toString();
    }
    
    
    
}