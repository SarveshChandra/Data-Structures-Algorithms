A Data Flow Diagram (DFD) is a graphical representation of the "flow" of data through an information system, modeling its process aspects. It's also often used as a preliminary step to create an overview of the system, which can later be elaborated.

Here are the major components of a DFD:

1. **Entities or Terminators:** These are data sources or destinations, often representing users or external systems that interact with the system you're modeling.

2. **Processes:** These are activities or functions that transform the data from one form to another.

3. **Data Stores:** These are places where data can be stored for later use.

4. **Data Flows:** These are the routes that data takes between the sources, processes, and stores.

DFDs can be categorized into levels:

- **Context Diagram (Level 0 DFD):** This is the top-level DFD that provides a summary-level view of a system. It shows the system boundaries, external entities that interact with the system, and the major data flows between them.
- **Level 1 DFD:** This shows how some part of the system is broken down into subsystems (processes), each of which deals with one or more data flows to or from external entities, and which together provide all of the functionality of the system as a whole.
- **Level 2 DFD:** They show more detail than a Level 1 DFD. Each Level 1 process can be broken down into more detailed Level 2 processes, showing more precise details of how the system operates.

For example, let's take a library management system. Here is a simple explanation of a Level 0 DFD:

1. **Entities:** The main entities involved in this system could be the Librarian and the Borrower.

2. **Process:** The system itself, i.e., the Library Management System, would be the central process.

3. **Data Flows:** For instance, the Borrower might issue a 'Book Request' to the system. The system, in turn, might give back a 'Borrowed Book' and a 'Due Date' for the book to be returned. 

The diagram would look something like this:

```text
 +--------+      Book Request       +-------------------+
 |        |  -------------------->  |                   |
 |        |                        | Library Management|
 |Borrower| <--------------------  |       System      |
 |        |   Borrowed Book, Due  |                   |
 |        |          Date         |                   |
 +--------+                        +-------------------+
                                         ^
                                         |
                                         |
                                    Librarian
```

Remember, this is a very simplified example, and actual DFDs could get a lot more complicated, especially as you go deeper into the system with Level 1 and Level 2 DFDs. But the basic idea will remain the same - DFDs are a way to visually represent how data flows through a system.