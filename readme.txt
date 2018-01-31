import java.util.Scanner;
import java.util.*;

class Node{
	 int data;
	 Node next;
	 
	 Node(){
		 data = 0;
		 next = null;
		    }
	 
	 Node(int a, Node n){
		 data = a;
		 next = n;
	 }

	 public void setnext(Node n){
		 next = n;
		 
	 }
	 
	 public void setdata(int a){
		 data = a;
	 }
	 
	 public Node getnext(){
		 return next;
	 }
	 
	 public int getdata(){
		 return data;
	 }
	 
		}
class list{
	Node head;
	Node temp;
	Node preptr;
	int size;
	
	list(){
		head = null;
		size = 0;
		}
	
	public void insert_atpos(int pos,int val){
		temp=head;
		Node ptr = new Node(val,null);
		int i = 0;
		while(i < pos){
			preptr=temp;
			temp=temp.getnext();
			i++;
		}
		preptr.setnext(ptr);
		ptr.setnext(temp);
	}
	
	public void insert_atend(int val){
		Node ptr = new Node(val,null);
		size++;
		if(head == null){
			head = ptr;
		}
		else{
			temp = head;
			while(temp.getnext() != null){
				temp=temp.getnext();
			}
			temp.setnext(ptr);
		}
	}

	public void insert_atbeg(int val){
		Node ptr = new Node(val,null);
		size ++;
		if(head == null)
		{
			head=ptr;
		}
		else{
			ptr.setnext(head);
			head = ptr;
		}
	}
	
	public void display(){
		if(size == 0){
			System.out.println("empty");
		}
		
		if(head.getnext() == null){
			System.out.println(head.getdata());
		return;
		}
		Node p = head;
		System.out.println(head.getdata());
		p=head.getnext();
		while(p.getnext() != null){
			System.out.println(p.getdata());
			p=p.getnext();
		}
		System.out.println(p.getdata());
		}
	
	
	public void delete_atbeg(){
		if(head == null){
			System.out.println("nothing to delete");
		}
		else{
			head = head.getnext();
		}
	}
	
	public void delete_atend(){
		if(head == null){
			System.out.println("nothing to delete");
		}
		else{
			temp = head;
			while(temp.getnext() != null){
				preptr = temp;
				temp=temp.getnext();
				}
				preptr.setnext(null);
	}
}
}
	
	 public class Linklist {
		 	static int i=0;
			public static void main(String[] args) {
				// TODO Auto-generated method stub
				Scanner c = new Scanner(System.in);
				list l = new list();
				while(i<5){
				System.out.println("insert data");
				l.insert_atend(c.nextInt());
				i++;
				}
				//l.delete_atend();
				System.out.println("pos,val");
				l.insert_atpos(c.nextInt(), c.nextInt());
				l.display();
				
		}
 }
		