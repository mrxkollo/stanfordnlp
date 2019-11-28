path = "/home/mkollo/Downloads/B1_Kaisa_1.txt"
with open(path, "r", encoding="utf8") as fp:
    with open("/home/mkollo/Downloads/_et_edt.dev.in.conllu", "a+", encoding="utf8") as wp:
        with open("/home/mkollo/Downloads/UD_Estonian-EDT/et_edt-ud-test.conllu") as dfp:
            for line in dfp:
                if "#" not in line:
                    wp.write("\t".join(line.split()) + "\n")

            for line in fp:
                if "#" not in line:
                    wp.write("\t".join(line.split()) + "\n")


