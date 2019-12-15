# MY IMPORT
import preprocessing_data
import k_means

# PYTHON IMPORT
from tkinter import *
import matplotlib.pyplot as plt


class GUI_k_means:
    def first_init(self):
        self.path_data.delete(0, END)
        self.columns.delete(0, END)
        self.num_clusters.delete(0, END)
        self.separator_csv.delete(0, END)

        self.path_data.insert(0, '/home/petr/Documents/test1.csv')
        self.path_data.focus_force()

        self.num_iter.insert(0, '1')
        self.num_iter.focus_force()

        self.separator_csv.insert(0, ';')
        self.separator_csv.focus_force()

        self.columns.insert(0, 'petal_length,petal_width,variety')
        self.columns.focus_force()

        self.num_clusters.insert(0, '3')
        self.num_clusters.focus_force()

        self.clu = []

    def solution(self):
        if (preprocessing_data.check_path_exists(self.path_data.get())):
            self.l_result['text'] = "File exist"
            try:
                self.clusters = float(self.num_clusters.get())
            except ValueError:
                self.l_result['text'] = "Error in clusters input"
                pass
        else:
            self.l_result['text'] = "Path to csv file doesn't exist or file is not csv."


        list_data = preprocessing_data.raw_data_as_list(self.path_data.get(), self.separator_csv.get())
        list_data = preprocessing_data.remove_empty_collumn(list_data)
        with open('out.txt', 'w+') as f:
            f.write(preprocessing_data.data_about_input_file(list_data,self.separator_csv.get(), self.path_data.get()))
        f.close


        list_data = preprocessing_data.remove_collumns_in_list(self.columns.get(), list_data, self.path_data.get(),
                                                               self.separator_csv.get())
        if list_data == -1:
            self.l_result['text'] = f"Omitted collumn not in data"
        elif all(type(x) is str for x in list_data[3]) == True:
            self.l_result['text'] = f"Data contain string."
        else:
            centroid, clusters, sum = k_means.k_means(list_data, self.num_clusters.get(), self.num_iter.get())
            SSE = k_means.SSE(centroid, clusters, self.num_clusters.get())
            tmp_name_ommited = self.columns.get().split(',')
            collumns_names = preprocessing_data.get_names_collumn(self.path_data.get(),self.separator_csv.get())
            self.l_result['text'] = f" Final centroid : {centroid} \n Num. recalculations : {sum} \n SSE: {SSE} \n Attributes: {list(set(collumns_names) - set(tmp_name_ommited))}"
            tmp = self.l_result['text']
            self.clu = clusters

        with open('out.txt', 'a+') as f:
            print(f'{ tmp }', file=f)
            for index in range(len(clusters)):
                print(f'Cluster {index}: {len(clusters[index])}', file=f)
        f.close

    def grapf(self):
        if self.clu == []:
            self.l_result['text'] = "No clusters to calculated."
        elif len(self.clu[0][0]) == 2:
            color = ['#ff0000', '#00ff00', '#0000ff', '#555555', '#bcbd22','#1affff','#ff1aff']
            x = []
            y = []
            for s, cl in enumerate(self.clu):
                for i in cl:
                    x.append(i[0])
                    y.append(i[1])
                plt.scatter(x, y, c=color[s])
                x = []
                y = []
            plt.show()


        elif len(self.clu[0][0]) == 3:
            from mpl_toolkits.mplot3d import Axes3D
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            color = ['#ff0000', '#00ff00', '#0000ff', '#555555', '#bcbd22','#1affff','#ff1aff']
            x = []
            y = []
            z = []
            for s, cl in enumerate(self.clu):
                for i in cl:
                    x.append(i[0])
                    y.append(i[1])
                    z.append(i[2])
                ax.scatter(x, y, z, c=color[s])
                x = []
                y = []
                z = []
            plt.show()

        else:
            pass

    def __init__(self, root):

        root.title('K_MEANS')

        self.top = Frame(root)
        self.top.pack(fill=BOTH, expand=1)

        self.inputdata = Frame(self.top, relief=GROOVE, borderwidth=2)
        self.inputdata.pack(fill=Y, side=LEFT, padx=4, pady=4, ipady=4)

        self.l_path = Label(self.inputdata, text="PATH to csv:")
        self.l_path.pack(fill=X, padx=1, pady=1)
        self.path_data = Entry(self.inputdata, width=40)
        self.path_data.pack(padx=8, pady=3)

        self.l_seperator = Label(self.inputdata, text="Separator in csv file:")
        self.l_seperator.pack(fill=X, padx=8, pady=1)
        self.separator_csv = Entry(self.inputdata, width=40)
        self.separator_csv.pack(padx=8, pady=3)

        self.l_ommitted = Label(self.inputdata, text="Omitted column(s) (separated by a comma):")
        self.l_ommitted.pack(fill=X, padx=8, pady=1)
        self.columns = Entry(self.inputdata, width=40)
        self.columns.pack(padx=8, pady=3)

        self.l_numclustors = Label(self.inputdata, text="Number of clusters:")
        self.l_numclustors.pack(fill=X, padx=8, pady=1)
        self.num_clusters = Entry(self.inputdata, width=40)
        self.num_clusters.pack(padx=8, pady=3)

        self.l_numiter = Label(self.inputdata, text="Number iterations:")
        self.l_numiter.pack(fill=X, padx=8, pady=1)
        self.num_iter = Entry(self.inputdata, width=40)
        self.num_iter.pack(padx=8, pady=3)


        self.first_init()

        self.vysf = Frame(self.top, relief=GROOVE, borderwidth=2)
        self.vysf.pack(fill=BOTH, padx=4, pady=4, expand=1, side=LEFT)

        self.lvys = Label(self.vysf, text="Result")
        self.lvys.pack()

        self.l_result = Label(self.vysf, text="No result", relief=SUNKEN, borderwidth=2)
        self.l_result.pack(fill=BOTH, padx=4, pady=4, ipadx=4, ipady=4)

        self.buttf = Frame(self.vysf)
        self.buttf.pack(fill=Y, side=BOTTOM)

        self.buttgrapf = Button(self.buttf, text="Graph", width=10, command=self.grapf)
        self.buttgrapf.pack(side=LEFT)

        self.buttv = Button(self.buttf, text="Solve", width=10, command=self.solution)
        self.buttv.pack(side=LEFT)

        self.buttk = Button(self.buttf, text="QUIT", width=10, command=root.quit)
        self.buttk.pack(side=RIGHT)


root = Tk()
app = GUI_k_means(root)
root.mainloop()
