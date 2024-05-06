import datetime
class ComplaintManagementSystem:
    def __init__(self):
        self.complaint={}

    def  new_Complaint(self,id,name,no,area):
        timestamp = datetime.datetime.now()
        self.complaint[id]={  "name":name,
                              "no":no,
                              "area":area,
                              "status":"Pending",
                              "time":timestamp }
        print("Complaint created Successfully")      

    def  update_Complaint(self,id,status):
        if id in self.complaint:
            self.complaint[id]["status"] = status
            print("Complaint updated Successfully")
        else:
            print("Complaint id not found")

    def view_Complaints(self):
        if len(self.complaint)==0:
            print("No Complaints to display")
        else:
            print("Complaints")
            for complaint_id, complaint in self.complaint.items():
                print(f"ID: {complaint_id}, User: {complaint['name']}, Number:{complaint['no']} , Area: {complaint['area']},Status: {complaint['status']}, Timestamp: {complaint['time']}"
            )
            print("Total No of Complaints:",len(self.complaint))    
            
    def delete_Complaints(self,id):
        if len(self.complaint)==0:
            print("No complaints to delete")
        else:
            del self.complaint['id']
            print("Complaint deleted successfully")    

cms=ComplaintManagementSystem()
while True:
    print("\nComplaint Management") 
    print("1.New Complaint")
    print("2.Update Complaint")
    print("3.View Complaint")
    print("4.Delete Complaint")
    print("5.Exit")

    choice=input("Enter the Choice[1-5]:")

    if choice=="1":
        id=input("Enter Complaint ID:")
        name=input("Enter your Name:")
        no=input("Enter your Number:")
        area=input("Enter your Area:")
        cms.new_Complaint(id,name,no,area)
    elif choice=="2":
        id=input("Enter Complaint ID:")
        status=input("Enter the status to update:")
        cms.update_Complaint(id,status) 
    elif choice=="3":
        cms.view_Complaints()
    elif choice=="4":
        id=input("Enter Complaint Id:")
        cms.delete_Complaints(id)
    elif choice=="5":
        print("Exiting the Console, Thank You!!")
        break
    else:
        print("Invalid Choice, Please select valid choice")
