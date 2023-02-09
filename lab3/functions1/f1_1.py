def grams_to_ounces(weight):
    new_weight = weight / 28.3495
    return new_weight

weight_in_grams = int(input())

weight_in_grams = grams_to_ounces(weight_in_grams)

print(f"{weight_in_grams} ounces")