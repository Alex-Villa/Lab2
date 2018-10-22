def merge(arr, l, m, r): #merge sorts the converted linked list now a python list and applys merge sort to sort from big counter value to small counter value
    n1 = m - l + 1
    n2 = r - m
    # create temp arrays
    L = []
    R = []
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L.append(arr[l+i])

    for j in range(0, n2):
        R.append(arr[m + 1 + j])
        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i].count >= R[j].count:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeSort(arr, l, r): #merge sorts the converted linked list now a python list and applys merge sort to sort from big counter value to small counter value
    m = (l + (r - 1)) // 2
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def bubbleSort(pythonList): #swaps pointers and values to sucessfully and properly do the bubblesort this case doing it in descending order (big counter value to small counter value)
    inode = pythonList.head
    while inode is not None:
        jnode = pythonList.head
        while jnode is not None:
            if jnode.count < inode.count:
                temppass = inode.password
                tempcounter = inode.count
                inode.password = jnode.password
                inode.count = jnode.count
                jnode.password = temppass
                jnode.count = tempcounter
            jnode = jnode.next
        inode = inode.next

def linkedListToPythonList(linkedList2): # converts the linked list into a python list to allow the merge sort to work as an array
    pythonList = []
    currNode = linkedList2.head
    lastNode = linkedList2.tail

    while True:
        pythonList.append(currNode)
        if currNode == lastNode:
            break
        currNode = currNode.next
    return pythonList

def ListAppend(list, newNode): #appends the password from the file into a node in linked list
    if list.head == None:
        list.head = newNode
        list.tail = newNode
    else:
        list.tail.next = newNode
        list.tail = newNode

def add(passwords, password, dict, solution): # adds to linked list distinguishes with method to use a loop to check if password is there of dictionary
    if solution == 1:
        dictionary(passwords, password, dict)
        return
    curNode = passwords.head
    while curNode is not None:
        if curNode.password == password:
            curNode.count += 1
            return
        curNode = curNode.next
    ListAppend(passwords, Node(password, 1, None))

def display(passwords): # used to display to bubblesort top 20 passwords
    curNode = passwords.head
    counter = 1
    stop_at = 20
    while curNode is not None:
        print("Password: '", curNode.password, "' appeared", curNode.count, "times")
        curNode = curNode.next
        if (counter == stop_at):
            break
        counter += 1

def fillDict(passwords, dict): #fills the dictionary to use for the linked list to see if a password is already in the dictionary and doesnt need to be added to list and dictionary
    for password in dict:
        ListAppend(passwords, Node(password, dict[password], None))

def dictionary(passwords, password, dict): #checks if password is already in list if so changes counter for that node in linked list
    if password in dict:
        dict[password] = dict[password] + 1
        curNode = passwords.head
        while curNode is not None:
            if curNode.password == password:
                curNode.count += 1
    else:
        dict[password] = 1

class Node(object): # node object
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next

class LinkedList: # used to create linked list
    def __init__(self):
        self.head = None
        self.tail = None

def getPasswords(passwords, solution): # reader that gets the passwords from the desired text file
    dict = {}
    try:
        with open('100-thousand-combos.txt', 'br') as f:
            '''i = 1'''
            for line in f:
                line = (line.decode('utf-8'))
                line = line.split()
                if len(line) > 1:
                    password = line[1].strip()
                    add(passwords, password, dict, solution)
            if solution == 1:
                fillDict(passwords, dict)
    except FileNotFoundError:
        print("I'm sorry, but the file cannot be found.")
        print("Please place the file in the folder with the program and label it '100-thousand-combos.txt' with .txt extension and start the program again.")
        quit()

def main():
    print("The program will notify you when it is done")
    print("\n*****************bubble sort top 20****************")
    passwords = LinkedList()
    getPasswords(passwords, 0)
    bubbleSort(passwords)
    display(passwords)

    print("*****************merge sort top 20****************")
    passwords = LinkedList()
    getPasswords(passwords, 1)
    pythonList = linkedListToPythonList(passwords)
    mergeSort(pythonList, 0, len(pythonList)-1)
    for i in range(20):
        print("Password: '", pythonList[i].password, "' appeared", pythonList[i].count, "times")
    print("\nThe program has finished")

main()