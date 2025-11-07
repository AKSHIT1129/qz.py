from tkinter import *
import random

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Sneaker Billing System")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.Air_Force = IntVar()
        self.Air_Jordan= IntVar()
        self.Dunk_Low = IntVar()
        self.Blazer_Mid = IntVar()
        self.Zoom_Mercurial = IntVar()
        self.Superstar = IntVar()
        self.Stan_Smith = IntVar()
        self.Gaz = IntVar()
        self.Samba = IntVar()
        self.Forum_84 = IntVar()
        self.ChuckTaylor = IntVar()
        self.OneStar = IntVar()
        self.ProLeather = IntVar()
        self.JackP = IntVar()
        self.StarPlayer = IntVar()
        self.total_Nike = StringVar()
        self.total_Adidas = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()


        #===================================
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Sneaker Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = bg_color,fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

        #==================Nike Frame=====================#
        F2 = LabelFrame(self.root,text = 'Nike',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Air Force")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Air_Force)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Air Jordan
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Air Jordan")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Air_Jordan)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Dunk Low
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Dunk Low")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Dunk_Low)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Blazer Mid
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Blazer Mid")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Blazer_Mid)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Zoom Mercurial
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Zoom Mercurial")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Zoom_Mercurial)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Adidas Frame=====================#
        F2 = LabelFrame(self.root,text = 'Adidas',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content
        Superstar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Superstar")
        Superstar_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        Superstar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Superstar)
        Superstar_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        Gaz_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Gazelle")
        Gaz_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        Gaz_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Gaz)
        Gaz_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        Stan_Smith_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Stan Smith")
        Stan_Smith_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        Stan_Smith_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Stan_Smith)
        Stan_Smith_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        Samba_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Samba")
        Samba_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        Samba_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Samba)
        Samba_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        Forum_84_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Forum 84")
        Forum_84_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        Forum_84_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Forum_84)
        Forum_84_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Other Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Converse',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content
        ChuckTaylor_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Chuck Taylor")
        ChuckTaylor_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        ChuckTaylor_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ChuckTaylor)
        ChuckTaylor_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "One Star")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.OneStar)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        ProLeather_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pro Leather")
        ProLeather_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        ProLeather_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.ProLeather)
        ProLeather_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Jack Purcell")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.JackP)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Star Player")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.StarPlayer)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height = 380)
        #===========
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Nike")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_Nike)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Adidas")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_Adidas)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Converse Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nike Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Adidas Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Converse Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

#Function to get total pSuperstars
    def total(self):
        #=================Total Nike PSuperstars
        self.total_Nike_pSuperstars = (
            (self.Air_Force.get() * 7000)+
            (self.Air_Jordan.get() * 13000)+
            (self.Dunk_Low.get() * 6500)+
            (self.Blazer_Mid.get() * 7500)+
            (self.Zoom_Mercurial.get() *8000)
        )
        self.total_Nike.set("Rs. "+str(self.total_Nike_pSuperstars))
        self.tax_cos.set("Rs. "+str(round(self.total_Nike_pSuperstars*0.05)))
        #====================Total Adidas PSuperstars
        self.total_Adidas_pSuperstars = (
            (self.Samba.get()*9000)+
            (self.Gaz.get() * 11000)+
            (self.Stan_Smith.get() * 8000)+
            (self.Superstar.get() *6000)+
            (self.Forum_84.get() * 12000)

        )
        self.total_Adidas.set("Rs. "+str(self.total_Adidas_pSuperstars))
        self.tax_groc.set("Rs. "+str(round(self.total_Adidas_pSuperstars*0.05)))
        #======================Total Other PSuperstars
        self.total_other_pSuperstars = (
            (self.ChuckTaylor.get() * 4000)+
            (self.ProLeather.get() * 7500)+
            (self.OneStar.get() * 5500)+
            (self.JackP.get() * 4500)+
            (self.StarPlayer.get() * 5000)
        )
        self.total_other.set("Rs. "+str(self.total_other_pSuperstars))
        self.tax_other.set("Rs. "+str(round(self.total_other_pSuperstars*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To DESI BOYS Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         PSuperstar")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and pSuperstar to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.Air_Force.get() != 0:
            self.txt.insert(END,f"\nAir Force         {self.Air_Force.get()}           {self.Air_Force.get() * 7000}")
        if self.Air_Jordan.get() != 0:
            self.txt.insert(END,f"\nAir Jordan        {self.Air_Jordan.get()}           {self.Air_Jordan.get() * 13000}")
        if self.Dunk_Low.get() != 0:
            self.txt.insert(END,f"\nDunk Low         {self.Dunk_Low.get()}           {self.Dunk_Low.get() * 6500}")
        if self.Blazer_Mid.get() != 0:
            self.txt.insert(END,f"\nBlazer Mid        {self.Blazer_Mid.get()}           {self.Blazer_Mid.get() * 7500}")
        if self.Zoom_Mercurial.get() != 0 :
            self.txt.insert(END,f"\nZoom Mercurial       {self.Zoom_Mercurial.get()}           {self.Zoom_Mercurial.get() * 8000}")
        if self.Samba.get() != 0:
            self.txt.insert(END,f"\nSamba             {self.Samba.get()}           {self.Samba.get() * 9000}")
        if self.Gaz.get() != 0:
            self.txt.insert(END,f"\nGazelle          {self.Gaz.get()}           {self.Gaz.get() * 11000}")
        if self.Stan_Smith.get() != 0:
            self.txt.insert(END,f"\nStan_Smith              {self.Stan_Smith.get()}           {self.Stan_Smith.get() * 8000}")
        if self.Superstar.get() != 0:
            self.txt.insert(END,f"\nSuperstar              {self.Superstar.get()}           {self.Superstar.get() * 6000}")
        if self.Forum_84.get() != 0:
            self.txt.insert(END,f"\nForum_84             {self.Forum_84.get()}           {self.Forum_84.get() * 12000}")
        if self.ChuckTaylor.get() != 0:
            self.txt.insert(END,f"\nChuck Taylor              {self.ChuckTaylor.get()}           {self.ChuckTaylor.get() * 4000}")
        if self.ProLeather.get() != 0:
            self.txt.insert(END,f"\nPro Leather            {self.ProLeather.get()}           {self.ProLeather.get() * 7500}")
        if self.OneStar.get() != 0:
            self.txt.insert(END,f"\nOne Star              {self.OneStar.get()}           {self.OneStar.get() * 5500}")
        if self.JackP.get() != 0:
            self.txt.insert(END,f"\nJackP             {self.JackP.get()}           {self.JackP.get() * 4500}")
        if self.StarPlayer.get() != 0:
            self.txt.insert(END,f"\nStar Player          {self.StarPlayer.get()}           {self.StarPlayer.get() * 5000}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : {self.total_Nike_pSuperstars+self.total_Adidas_pSuperstars+self.total_other_pSuperstars+self.total_Nike_pSuperstars * 0.05+self.total_Adidas_pSuperstars * 0.05+self.total_other_pSuperstars * 0.05}")


    #Function to exit
    def exit(self):
        self.root.destroy()

    #Function To Clear All Fields


        


root = Tk()
object = Bill_App(root)
root.mainloop()
