def drainage_basins(elavation_ridge):
    def drainage_basins_helper(elavation_ridge, ctr):
        if ctr == len(elavation_ridge) - 1:
            if elavation_ridge[ctr] < elavation_ridge[ctr - 1]:
                return [ctr]
            else:
                return []
        if ctr == 0 and elavation_ridge[ctr] < elavation_ridge[ctr + 1]:
            return [ctr] + drainage_basins_helper(elavation_ridge, ctr + 1)

        if elavation_ridge[ctr] < elavation_ridge[ctr - 1] and \
                elavation_ridge[ctr] < elavation_ridge[ctr + 1]:
            return [ctr] + drainage_basins_helper(elavation_ridge, ctr + 1)

        else:
            return drainage_basins_helper(elavation_ridge, ctr + 1)

    return drainage_basins_helper(elavation_ridge, 0)


print(drainage_basins([2, 3, 1, 4, 2, 5, 6, 1, 6, 5, 4, 4, 2]))
print(drainage_basins([0, 0, 0]))
