import java.util.Scanner;

public class Test_Info {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int cursor = 0;

        while (cursor == 0) {
            System.out.println("------MENU------");
            System.out.println("1. Staff");
            System.out.println("2. Student");
            System.out.println("3. Exit");
            System.out.println("-----------------");

            int input = sc.nextInt();

            if (input == 1) {
                // Staff

                System.out.print("Name: ");
                String nam = sc.next();
                System.out.print("Address: ");
                String addr = sc.next();
                System.out.print("Email: ");
                String email = sc.next();
                System.out.print("Ph_No: ");
                int ph_no = sc.nextInt();
                System.out.print("Designation: ");
                String desig = sc.next();
                System.out.print("Emp_id: ");
                String emp_id = sc.next();
                System.out.print("Company: ");
                String company = sc.next();

                System.out.println("Salary: ");
                int sal = sc.nextInt();

                Staff staff = new Staff(nam, addr, email, ph_no, desig, emp_id, company);

                int salary = staff.Salary(sal);
                System.out.println("Salary: " + salary);

            }

            if (input == 2) {
                // Student

                System.out.print("Name: ");
                String nam = sc.next();
                System.out.print("Address: ");
                String addr = sc.next();
                System.out.print("Email: ");
                String email = sc.next();
                System.out.print("Ph_No: ");
                int ph_no = sc.nextInt();
                System.out.print("USN: ");
                String USN = sc.next();
                System.out.print("Branch: ");
                String branch = sc.next();

                System.out.println("Fee: ");
                int f = sc.nextInt();

                Student staff = new Student(nam, addr, email, ph_no, USN, branch);

                int salary = staff.Fee(f);
                System.out.println("Fee: " + salary);

            }

            if (input == 3) {
                cursor = 1;
                break;
            }

            if (input > 3 && input < 1) {
                System.out.println("Invalid Input");
            }
        }

    }

}

class Person {
    String name, addr, email;
    int ph_no;

    // Default Constructor
    Person() {
    }

    // With Paramiters
    Person(String name, String addr, String email, int ph_no) {
        this.addr = addr;
        this.email = email;
        this.name = name;
        this.ph_no = ph_no;
    }
}

// Staff
interface Staff_Op {
    public int Salary(int s);
}

class Staff extends Person implements Staff_Op {
    String company, emp_id, desig;

    Staff(String nam, String addr, String email, int ph_no, String desig, String emp_id, String company) {
        super(nam, addr, email, ph_no);
        this.name = nam;
        this.addr = addr;
        this.email = email;
        this.ph_no = ph_no;
        this.desig = desig;
        this.emp_id = emp_id;
        this.company = company;

        System.out.print(this.name + " " + this.addr + " " + this.company + " " + this.desig + " " + this.email + " "
                + this.emp_id + " " + this.ph_no);
    }

    @Override
    public int Salary(int s) {
        return s + 100000;
    }
}

// Student
interface Fee_Op {
    public int Fee(int f);
}

class Student extends Person implements Fee_Op {
    String USN, branch;

    Student(String nam, String addr, String email, int ph_no, String USN, String branch) {
        super(nam, addr, email, ph_no);
        this.name = nam;
        this.addr = addr;
        this.email = email;
        this.ph_no = ph_no;
        this.USN = USN;
        this.branch = branch;

        System.out.print(
                this.name + " " + this.addr + " " + this.USN + " " + this.branch + " " + this.email + " " + this.ph_no);
    }

    @Override
    public int Fee(int f) {
        return f + 10000;
    }

}
