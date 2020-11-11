# Making valid data from text-table
# from https://isu.ifmo.ru/pls/apex/f?p=2143:DEP:102384079894805::NO::BUN_BUN_ID,STR_STR_ID,UBU_UBU_ID:1000079,85,
with open("Students.txt", "r") as file:
    data = file.readlines()
    out_put = open("StudentsList.txt", "w")
    for i in data:
        boxes = i.split("\t")[:2]
        fio_long = boxes[0].split()
        if len(fio_long) == 3:
            fio = "{} {}.{}.".format(fio_long[0], fio_long[1][0], fio_long[2][0])
        else:
            fio = "{} {}.".format(fio_long[0], fio_long[1][0])
        out_put.write("{} {}\n".format(fio, boxes[1]))
