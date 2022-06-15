import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Hw2_pt1 {

    public static int gpaBelow(Student[] students, double g) {
        // implement this method

        /**
         * for-loop used to check if each user has gpa below g, if true: user count is added to totalStudents(counter variable)
         */
        int totalStudents = 0;
        for(Student student : students) {
            if(student.getGPA()<(g)) {
                System.out.println(student);
                ++totalStudents;
            }
        }

        /**
         * checks to see if there are any students with gpa below g
         */
        if(totalStudents == 0) {
            System.out.println("No students with gpa lower than" + g);
        }
        return totalStudents;
    }

    public static void main(String[] args) throws IOException {

        // create an array of Student objects
        /**
         * StudentArray stores int 10 for 10 students. Array students stores the students
         */
        int StudentArray = 10;
        Student[] students = new Student[StudentArray];

        // read input file and create and store Student objects in the array
        /**
         * searches text file. will return error if file not found
         */
        Scanner fileScanner = new Scanner(new File("student_input.txt"));

        /**
         * for-loop used to read each line and removes spaces and commas. Then appended in student array.
         */
        for (int i = 0; i < StudentArray; ++i) {
            String[] data = fileScanner.nextLine().strip().split(", ");
            students[i] = new Student(data[0].strip(), data[1].strip(), Double.parseDouble(data[2].strip()));
        }
        fileScanner.close();

        System.out.println("\nAll students:");
        for (Student student : students) {
            System.out.println(student);
        }

        double gpa = 3.0;

        System.out.println("\nAll students with GPA below " + gpa);

        int numStudents = gpaBelow(students, gpa);
        System.out.println("\nNumber of students with gpa below " + gpa + " is: " + numStudents);


    }

}

class Student {

    private String name;
    private String major;
    private double GPA;

    public Student() { }

    public Student(String name, String major, double GPA) {
        this.name = name;
        this.major = major;
        this.GPA = GPA;
    }

    public String getName() { return name; }
    public String getMajor() { return major; }
    public double getGPA() { return GPA; }

    public void setName(String name){
        this.name = name;
    }
    public void setMajor(String major) {
        this.major = major ;
    }
    public void setGPA(double GPA){
        this.GPA = GPA;
    }

    public String toString() {
        String s = "\tName = " + name +
                ",  Major = " + major +
                ",  GPA = " + GPA;
        return s;
    }


}

