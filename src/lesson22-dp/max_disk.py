# MaxDisk

import time

# Dati n file di dimensioni s1,s2,...,sn e un disco di capacita C, 
# vogliamo trovare un sottoinsieme dei file che pu`o essere
# memorizzato sul disco e che massimizza lo spazio usato.

def maxDisk_rec(disk_size, files):
    # 14s
    print(f"disk: {disk_size} - files: {files}")
    if len(files) == 0:
        return 0
    last_file = files[-1]
    max = maxDisk_rec(disk_size, files[:-1])
    if last_file <= disk_size:
        alt_max = last_file + maxDisk_rec(
                            disk_size-last_file,
                            files[:-1]
                            )
        if alt_max > max:
            max = alt_max
    return max

def maxDisk_rec_memo(disk_size, last_file_pos, files, memo):
    # 
    print(f"lastpos:{last_file_pos} - size:{disk_size}")
    print(f"{memo}")
    if memo[last_file_pos][disk_size] == -1:
        if last_file_pos  == 0:
            memo[0][disk_size] = 0
        else:
            max = maxDisk_rec_memo(disk_size, last_file_pos-1, files, memo)
            last_file = files[last_file_pos]
            if last_file <= disk_size:
                alt_max = last_file + maxDisk_rec_memo(
                                    disk_size-last_file,
                                    last_file_pos-1,
                                    files,
                                    memo
                                    )
                if alt_max > max:
                    max = alt_max
                print(f"max: {max} - alt_max: {alt_max}")
            memo[last_file_pos][disk_size] = max
    return memo[last_file_pos][disk_size]

def dp(files, c):
    t = [[0 for i in range(c + 1)] for i in range(len(files))]
    for i in range(1, len(files)):
        for j in range(0, c+1):
            t[i][j] = t[i-1][j]
            if files[i] <= j and t[i][j] <= files[i] + t[i-1][j - files[i]]:
                t[i][j] = files[i] + t[i-1][j - files[i]]
    #for i in range(len(t)):
    #    print(f"{i}:{t[i]}")
    return t[len(files)-1][c]


def main():

    disk_size = 10
    files = [1,5,3,4,2,2,7,3,5,6,7,8,1,2,3,4,4,4,8,19,9,21,3,1]

    memo = [[-1] * int(disk_size+1)] * int(len(files))

    print(f"memo: {len(memo)} - {len(memo[0])}")

    t0 = time.perf_counter()
    #print(f"maxD: {maxDisk_rec(disk_size, files)}")
    t1 = time.perf_counter() - t0
    print(f"Elapsed time: {t1}")


    t0 = time.perf_counter()
    print(f"maxD: {maxDisk_rec_memo(disk_size, len(files)-1, files, memo)}")
    t1 = time.perf_counter() - t0
    print(f"Elapsed time: {t1}")

    for i in range(len(memo)):
        print(f"{i}:{memo[i]}")

    print(dp(files, disk_size))

main()


