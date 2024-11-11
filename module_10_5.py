import multiprocessing
from _datetime import datetime


def  read_info(name):
    all_data = []
    file = open(name, 'r', encoding= 'utf - 8')
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line)
    file.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]
print(filenames)


# Линейный вызов
start = datetime.now()

for i in filenames:
    read_info(i)

fin = datetime.now()
print((fin - start), '(линейный)')   # 0:00:04.273544 (линейный)

# Многопроцессный
if __name__ == '__main__':
    start = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    fin = datetime.now()
    print((fin - start), '(многопроцессный)')  # 0:00:01.976714 (многопроцессный)

