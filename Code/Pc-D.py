from tkinter import *
#window
Pcd = Tk()
Pcd.title('Pc DataBase')
Pcd.geometry('160x300')
Pcd.config(bg='#242020')
#functions
def gpu():
    #gpu window
    gpu= Toplevel(Pcd)
    gpu.title("Gpu_Select")
    gpu.config(bg='#242020')
    gpu.geometry("150x170")
    #functions
    def ngpu():
        ngpu = Toplevel(Pcd)
        variable = StringVar(ngpu)
        variable.set("2080ti")
        ngpu.geometry('150x100')
        def subm():
            cgpu = Toplevel(Pcd)
            
            lbl8 = Label(cgpu, text='N/A')
            lbl8.grid(row=1,column=1)
            a = variable.get()
            teti= open('Nvidia-2080ti.txt', 'r')
            asdf = open('Nivida_Geforce_930a.txt','r')
            
                    
            if a == "RTX 2080ti":
                    lbl8.config(text = teti.readlines())
            if a == "GTX 930A":
                    lbl8.config(text = asdf.readlines())
                
                


            

                
            
        sub = Button(ngpu, text='submit',command=subm)
        sub.grid()
        nv = OptionMenu(ngpu, variable, "RTX 2080ti", "RTX 2080s", "RTX 2080", "RTX 2070TI", "RTX 2070s", "RTX 2070","GTX 930A")
        nv.grid()

    def rgpu():
        rgpu = Toplevel(Pcd)
    global photo2
    #buttons
    nvidia=Button(gpu,text="NVidia",bg='#242020',highlightthickness=0,bd=0,image=photo2, font=('Arial',36), command=ngpu)
    nvidia.grid(row=1,column=1)
    radeon=Button(gpu,text="Radeon",bg='#242020',highlightthickness=0,bd=0,image=photo3, font=('Arial',36), command=rgpu)
    radeon.grid(row=2,column=1)
def cpu():
    cpu= Toplevel(Pcd)
    
#Labels
main = Label(Pcd, text = 'PC-database',bg="#242020",fg='#000000',font=( "Ariel", 20))
main.grid(columnspan=4)
#Icons
photo4 = PhotoImage(file="CPU.png")
photo3 = PhotoImage(file="Radeon.png")
photo2 = PhotoImage(file="Nvidia.png")
photo = PhotoImage(file= "GPU.png")
#buttons
gpus = Button(Pcd, text="GPU's",image = photo,bg='#242020',highlightthickness=0,bd=0, font=('Ariel',36), height=100, width = 150, command=gpu)
gpus.grid(rowspan=2)
cpus = Button(Pcd, text="CPU's", image = photo4, bg='#242020',highlightthickness=0,bd=0, font=('Ariel',36), height=150, width = 150, command=cpu)
cpus.grid(rowspan=3)
Pcd.mainloop()
