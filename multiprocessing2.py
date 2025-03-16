import time
import multiprocessing
import threading

EMPLOYEES = ["Иван", "Петр", "Сергей",]

threading_results = []
multiprocessing_results = []

def calculate_zp(employee, last_name_employee, queue=None):
    print(f"{employee} - {last_name_employee}: \n -------------")
    time.sleep(2)

    # for i in range(90_000_000):
    #     a = 1
    #     b = 2
    #     c = a + b


    print('Расчитать часы')
    print("Расчитать налоги")

    #для многопоточности
    threading_results.append(employee)

    #для многопроцессорности
    if queue:
        queue.put(employee)
    return employee



def main():
    for employee in EMPLOYEES:
        calculate_zp(employee, "Фамилия")

def main_with_multiprocessing():
    processes = []

    result_queue = multiprocessing.Queue()

    for employee in EMPLOYEES:
        processes.append(
            multiprocessing.Process(target=calculate_zp, args=(employee, "Фамилия", result_queue))
        )

    for process in processes:
        process.start()


    for process in processes:
        process.join()

    while not result_queue.empty():
        multiprocessing_results.append(result_queue.get())

    print(multiprocessing_results)


def main_with_threading():
    threads = []
    for employee in EMPLOYEES:
        threads.append(
            threading.Thread(target=calculate_zp, args=(employee, "Фамилия"))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start_time = time.time()
    # main()
    # main_with_multiprocessing()
    main_with_threading()

    print(threading_results)


    print(f"Время выполнения: {time.time() - start_time}")



