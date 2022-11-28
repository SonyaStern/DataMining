import matplotlib.pyplot as plt
import time
from miningDataStreams.Triest_Base import Triest_Base
from miningDataStreams.Triest_Impr import Triest_Impr

if __name__ == '__main__':
    file_name = "./data/CA-HepTh.txt"
    # M = [100, 200, 300,  500, 700, 1000]
    M = [200, 500, 700, 1000, 1500, 2000, 5000, 10000, 15000, 22000, 30000]
    # M = [1000, 5000, 10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000]
    # M = [1000, 5000, 10000, 20000, 40000, 100000]
    estimations = []
    estimations_impr = []
    global_start = time.time()
    for m in M:
        print("=====================" + str(m) + "=====================")
        start = time.time()
        triest_base = Triest_Base(m)
        global_t, global_triangle_count = Triest_Base.process_file(triest_base, file_name)
        estimations.append(global_triangle_count)
        end = time.time() - start
        print("BASE: Global T " + str(m) + ": " + str(global_t))
        print("BASE: Global triangle count with M " + str(m) + ": " + str(global_triangle_count))
        print("BASE: Spent time " + str(round(end, 3)) + "s.\n")

        triest_impr = Triest_Impr(m)
        start = time.time()
        global_t_impr = Triest_Impr.process_file(triest_impr, file_name)
        estimations_impr.append(global_t_impr)
        end = time.time() - start
        print("IMPR: Global T with M " + str(m) + ": " + str(global_t_impr))
        print("IMPR: Spent time " + str(round(end, 3)) + "s.\n")

    global_end = time.time() - global_start
    print("Spent time " + str(round(global_end, 3)) + "s.")
    plt.plot(M, estimations)
    plt.show()

    plt.plot(M, estimations_impr)
    plt.show()
