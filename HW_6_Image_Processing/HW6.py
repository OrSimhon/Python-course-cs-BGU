# *************** HOMEWORK 6 ***************
# GOOD LUCK!

# ********************* Helper functions ***********************
import matplotlib.pyplot as plt


def display(image):
    plt.figure()
    plt.imshow(image, cmap="gist_gray")
    # plt.show()


def is_zero_se(se):
    return se == [[0] * len(se)] * len(se[0])


# ************************ QUESTION 1 **************************
def load_binary_image(img_path):
    f = open(img_path, 'r')
    return [[int(ch) for ch in line.strip()] for line in f]


# ************************ QUESTION 2 **************************
def add_padding(image, padding):
    pad_image = []

    # Upper pad
    for i in range(padding):
        pad_image.append([0] * (len(image) + padding * 2))

    # Width pad
    for line in image:
        pad_line = [0] * padding + line + [0] * padding
        pad_image.append(pad_line)

    # Lower pad
    for i in range(padding):
        pad_image.append([0] * (len(image) + padding * 2))

    return pad_image


# ************************ QUESTION 3 **************************
def erosion(img_path, structuring_element):
    img_operated = load_binary_image(img_path)

    if is_zero_se(structuring_element):
        return img_operated
    padded = add_padding(img_operated, 1)
    vertical_window = len(padded) - len(structuring_element)  # Final vertical window position
    horizontal_window = len(padded[0]) - len(structuring_element[0])  # Final horizontal window position

    vertical_pos = 0
    while vertical_pos <= vertical_window:
        horizontal_pos = 0

        while horizontal_pos <= horizontal_window:
            erosion_flag = False
            for i in range(len(structuring_element)):
                for j in range(len(structuring_element[0])):
                    if structuring_element[i][j] == 1:
                        if padded[vertical_pos + i][horizontal_pos + j] == 0:
                            erosion_flag = True
                            break
                # if there is bi natch found, turn off the pixel
                if erosion_flag:
                    img_operated[vertical_pos][horizontal_pos] = 0
                    break
            horizontal_pos += 1
        vertical_pos += 1
    return img_operated


# ************************ QUESTION 4 **************************
def dilation(img_path, structuring_element):
    img_operated = load_binary_image(img_path)

    if is_zero_se(structuring_element):
        return img_operated
    padded = add_padding(img_operated, 1)
    vertical_window = len(padded) - len(structuring_element)  # Final vertical window position
    horizontal_window = len(padded[0]) - len(structuring_element[0])  # Final horizontal window position

    vertical_pos = 0
    while vertical_pos <= vertical_window:
        horizontal_pos = 0

        while horizontal_pos <= horizontal_window:
            dilation_flag = False
            for i in range(len(structuring_element)):
                for j in range(len(structuring_element[0])):
                    if structuring_element[i][j] == 1:
                        if padded[vertical_pos+i][horizontal_pos+j] == 1:
                            dilation_flag = True
                            break

                if dilation_flag:
                    img_operated[vertical_pos][horizontal_pos] = 1
                    break
            horizontal_pos += 1
        vertical_pos += 1
    return img_operated


img = load_binary_image('example.txt')
structural_element = load_binary_image('structuring_element.txt')
erode_img = erosion('example.txt', structural_element)
dilated_img = dilation('example.txt', structural_element)

display(img)
display(structural_element)
display(erode_img)
display(dilated_img)
plt.show()
