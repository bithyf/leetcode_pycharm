def rearrangeBarcodes(barcodes):
    from collections import Counter
    dict_barcodes = Counter(barcodes)
    dict_barcodes = sorted(dict_barcodes.items(), key=lambda x: -x[1])

    i = 0
    for barcode in dict_barcodes:
        length = barcode[1]
        while length > 0:
            barcodes[i] = barcode[0]
            length -= 1
            i = i + 2 if i + 2 < len(barcodes) else 1

    return barcodes


test = [1, 1, 1, 3, 2, 2]

print(rearrangeBarcodes(test))
