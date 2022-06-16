import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Hw2_p2 {
    // Reading data from txt file using scanner
    void readAndAddToList(String filePath, MyLinkedList<Car> linkedList) throws FileNotFoundException {
        Scanner sc = new Scanner(new File(filePath));

        /**
         * Loop through all the data present in car_info.txt.
         * removes all commas in each line
         */
        while (sc.hasNext()) {
            String[] str = sc.nextLine().split(", ");
            linkedList.addFirst(new Car(str[0], str[1], Integer.parseInt(str[2]), Integer.parseInt(str[3])));
        }
    }

    int olderThan(MyLinkedList<Car> linkedList, int yr) throws CloneNotSupportedException {
        // creates list of cars based on user input
        MyLinkedList<Car> ansList = new MyLinkedList();

        /**
         * Variable used to loop through the list and then checks to see if condition is true and adds car to list.
         */
        MyLinkedList.Node<Car> foo = linkedList.head;
        while (foo != null && foo.getElement() != null) {
            Car car = foo.getElement();
            if (yr > car.getYear()) {
                ansList.addFirst(car);
            }
            foo = foo.getNext();
        }

        /**
         * if no car is found, then a message will print
         */
        if (ansList.size == 0) {
            System.out.println("There are no car older then the year " + yr);
            return 0;
        }

        System.out.println("All cars older than " + yr);
        System.out.println(ansList);
        return ansList.size;
    }
    public static void main(String[] args) throws FileNotFoundException, CloneNotSupportedException {
        MyLinkedList<Car> linkedList = new MyLinkedList();
        Hw2_p2 carFoo = new Hw2_p2();

        carFoo.readAndAddToList("car_info.txt", linkedList);

        System.out.println("All cars");
        System.out.println(linkedList);
        System.out.println("Number of students older than 2015 is: " + carFoo.olderThan(linkedList, 2015));
    }
}

/*
 * Copyright 2014, Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser
 *
 * Developed for use with the book:
 *
 *    Data Structures and Algorithms in Java, Sixth Edition
 *    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
 *    John Wiley & Sons, 2014
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Original file name is SinglyLinkedList.
 * Modified for an assignment
 */

/**
 * A basic singly linked list implementation.
 *
 * @author Michael T. Goodrich
 * @author Roberto Tamassia
 * @author Michael H. Goldwasser
 */

class MyLinkedList<E> implements Cloneable {
    //---------------- nested Node class ----------------
    /**
     * Node of a singly linked list, which stores a reference to its
     * element and to the subsequent node in the list (or null if this
     * is the last node).
     */
    protected static class Node<E> {

        /** The element stored at this node */
        private E element;            // reference to the element stored at this node

        /** A reference to the subsequent node in the list */
        private Node<E> next;         // reference to the subsequent node in the list

        /**
         * Creates a node with the given element and next node.
         *
         * @param e  the element to be stored
         * @param n  reference to a node that should follow the new node
         */
        public Node(E e, Node<E> n) {
            element = e;
            next = n;
        }

        // Accessor methods
        /**
         * Returns the element stored at the node.
         * @return the element stored at the node
         */
        public E getElement() { return element; }

        /**
         * Returns the node that follows this one (or null if no such node).
         * @return the following node
         */
        public Node<E> getNext() { return next; }

        // Modifier methods
        /**
         * Sets the node's next reference to point to Node n.
         * @param n    the node that should follow this one
         */
        public void setNext(Node<E> n) { next = n; }
    } //----------- end of nested Node class -----------

    // instance variables of the SinglyLinkedList
    /** The head node of the list */
    protected Node<E> head = null;               // head node of the list (or null if empty)

    /** The last node of the list */
    protected Node<E> tail = null;               // last node of the list (or null if empty)

    /** Number of nodes in the list */
    protected int size = 0;                      // number of nodes in the list

    /** Constructs an initially empty list. */
    public MyLinkedList() { }              // constructs an initially empty list

    // access methods
    /**
     * Returns the number of elements in the linked list.
     * @return number of elements in the linked list
     */
    public int size() { return size; }

    /**
     * Tests whether the linked list is empty.
     * @return true if the linked list is empty, false otherwise
     */
    public boolean isEmpty() { return size == 0; }

    /**
     * Returns (but does not remove) the first element of the list
     * @return element at the front of the list (or null if empty)
     */
    public E first() {             // returns (but does not remove) the first element
        if (isEmpty()) return null;
        return head.getElement();
    }

    /**
     * Returns (but does not remove) the last element of the list.
     * @return element at the end of the list (or null if empty)
     */
    public E last() {              // returns (but does not remove) the last element
        if (isEmpty()) return null;
        return tail.getElement();
    }

    // update methods
    /**
     * Adds an element to the front of the list.
     * @param e  the new element to add
     */
    public void addFirst(E e) {                // adds element e to the front of the list
        head = new Node<>(e, head);              // create and link a new node
        if (size == 0)
            tail = head;                           // special case: new node becomes tail also
        size++;
    }

    /**
     * Adds an element to the end of the list.
     * @param e  the new element to add
     */
    public void addLast(E e) {                 // adds element e to the end of the list
        Node<E> newest = new Node<>(e, null);    // node will eventually be the tail
        if (isEmpty())
            head = newest;                         // special case: previously empty list
        else
            tail.setNext(newest);                  // new node after existing tail
        tail = newest;                           // new node becomes the tail
        size++;
    }

    /**
     * Removes and returns the first element of the list.
     * @return the removed element (or null if empty)
     */
    public E removeFirst() {                   // removes and returns the first element
        if (isEmpty()) return null;              // nothing to remove
        E answer = head.getElement();
        head = head.getNext();                   // will become null if list had only one node
        size--;
        if (size == 0)
            tail = null;                           // special case as list is now empty
        return answer;
    }

    @SuppressWarnings({"unchecked"})
    public boolean equals(Object o) {
        if (o == null) return false;
        if (getClass() != o.getClass()) return false;
        MyLinkedList other = (MyLinkedList) o;   // use nonparameterized type
        if (size != other.size) return false;
        Node walkA;                               // traverse the primary list
        walkA = head;
        Node walkB = other.head;                         // traverse the secondary list
        while (walkA != null) {
            if (!walkA.getElement().equals(walkB.getElement())) return false; //mismatch
            walkA = walkA.getNext();
            walkB = walkB.getNext();
        }
        return true;   // if we reach this, everything matched successfully
    }

    @SuppressWarnings({"unchecked"})
    public MyLinkedList<E> clone() throws CloneNotSupportedException {
        // always use inherited Object.clone() to create the initial copy
        MyLinkedList<E> other = (MyLinkedList<E>) super.clone(); // safe cast
        if (size > 0) {                    // we need independent chain of nodes
            other.head = new Node<>(head.getElement(), null);
            Node<E> walk = head.getNext();      // walk through remainder of original list
            Node<E> otherTail = other.head;     // remember most recently created node
            while (walk != null) {              // make a new node storing same element
                Node<E> newest = new Node<>(walk.getElement(), null);
                otherTail.setNext(newest);     // link previous node to this one
                otherTail = newest;
                walk = walk.getNext();
            }
        }
        return other;
    }

    public int hashCode() {
        int h = 0;
        for (Node walk=head; walk != null; walk = walk.getNext()) {
            h ^= walk.getElement().hashCode();      // bitwise exclusive-or with element's code
            h = (h << 5) | (h >>> 27);              // 5-bit cyclic shift of composite code
        }
        return h;
    }

    /**
     * Produces a string representation of the contents of the list.
     * This exists for debugging purposes only.
     */
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node<E> walk = head;
        while (walk != null) {
            sb.append(walk.getElement());
            if (walk != tail)
                sb.append("\n");
            walk = walk.getNext();
        }
        sb.append("\n");
        return sb.toString();
    }
}


class Car {

    private String VIN;
    private String make;
    private int year;
    private int price;

    public Car() { }

    public Car(String VIN, String make, int year, int price) {
        this.VIN = VIN;
        this.make = make;
        this.year = year;
        this.price = price;
    }

    public String getVIN() { return VIN; }
    public String getMake() { return make; }
    public int getYear() { return year; }
    public int getPrice() { return price; }

    public void setVIN(String VIN){
        this.VIN = VIN;
    }
    public void setMake(String make) {
        this.make = make ;
    }
    public void setYear(int year){
        this.year = year;
    }
    public void setPrice(int price){
        this.price = price;
    }


    public String toString() {
        String c = "\tVIN = " + VIN +
                "\tMake = " + make +
                "\tYear = " + year +
                "\tPrice = " + price;
        return c;
    }

}