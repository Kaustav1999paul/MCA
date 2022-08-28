import java.util.Scanner;

public class StudentInfo {
	String name, address,emailid,branch;
    int phoneno;
	double tfees, ad_fee,tution_fees,fee1;
	
	private void Student_details(String name2, String add, int phoneno2, String emailid2, String branch2) {
		this.name =name2;
		this.address = add;
		this.phoneno = phoneno2;
		this.emailid = emailid2;
		this.branch = branch2;	

        System.out.println("-----------------------");
        System.out.println("Student Info:");
        System.out.println();
        System.out.println("Name: "+ this.name);
        System.out.println("Address: "+ this.address);
        System.out.println("Phone: "+ this.phoneno);
        System.out.println("Email: "+ this.emailid);
        System.out.println("Branch: "+ this.branch);
        System.out.println("-----------------------");
        System.out.println();
        System.out.println();

	}
	
	public double fee(String branch2, double ad_fees, double tution_fees2, double bran_fees, double fee12) {
		this.ad_fee = ad_fees;
		this.tution_fees = tution_fees2;
		this.fee1 = fee12;
		tfees = ad_fee+tution_fees+fee1;
		if(branch.equalsIgnoreCase("BE")) {
			tfees+= bran_fees;
		}
		return tfees;
	}
	
	public static void main(String args[]) {
		StudentInfo si = new StudentInfo();
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the student details");
        System.out.println("-------------------------");
		System.out.println("enter the name");
		String name = sc.next();
		System.out.println("enter the address");
		String add = sc.next();
		System.out.println("enter the phoneno");
		int phoneno = sc.nextInt();
		System.out.println("enter the emailid");
		String emailid = sc.next();
		System.out.println("enter the branch");
		String branch = sc.next();
        si.Student_details(name,add,phoneno,emailid,branch);



		
		System.out.println("enter the admission fees");
		double ad_fees = sc.nextDouble();
		System.out.println("enter the tution fees");
		double tution_fees= sc.nextDouble();
		System.out.println("enter the branch fees");
		double bran_fees = sc.nextDouble();
		System.out.println("enter the Internet fee");
		double fee1 = sc.nextDouble();
		
		double tfee = si.fee(branch,ad_fees,tution_fees,bran_fees,fee1);
		
        System.out.println();
        System.out.println("-----------------------");
		System.out.println("total fees for the student is: "+tfee);
        System.out.println("-----------------------");
        System.out.println();
		
	}
}