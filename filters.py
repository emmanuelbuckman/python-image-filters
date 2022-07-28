import image_io
import copy


image_matrix = image_io.read_file('images/obama.png')


def red_stripes(image_matrix):
    image_matrix = image_io.read_file('python-image-filters/images/obama.png')
    count = 0
    for row in image_matrix:
        count += 1
        if count > 0:
            for col in row:
                col[0] = 255
        if count == 50:
            count = -50
        if count < 0:
            continue
    return image_matrix

result_matrix = red_stripes(image_matrix)
image_io.write_to_file('stripes.png', result_matrix)


# red_stripes('images/obama.png')

def grayscale(image_matrix):
    for row in image_matrix:
        for col in row:
            avg = int((sum(col)) / (len(col)))
            col[0] = avg
            col[1] = avg
            col[2] = avg
    return image_matrix

result_matrix = grayscale(image_matrix)
image_io.write_to_file('images/obama.png', result_matrix)

# grayscale('python-image-filters/images/flowers.jpeg')

image_matrix = image_io.read_file('images/obama.png')


def invert_colors(image_matrix):
    for row in image_matrix:
        for col in row:
            col[0] = 255 - col[0]
            col[1] = 255 - col[1]
            col[2] = 255 - col[2]
    return image_matrix
    # result_matrix = filters.invert_colors(image_matrix)
    # image_io.write_to_file('outputs/invert.png', result_matrix)


# invert_colors('images/obama.png')

def flip(image_matrix):
    image_matrix.reverse()
    return image_matrix
    # result_matrix = filters.flip(image_matrix)
    # image_io.write_to_file('outputs/flip.png', result_matrix)



def sepia(image_matrix):
    temp = []
    for row in range(len(image_matrix)):
        print(temp)
        for col in range(len(image_matrix[row])):
            temp = image_matrix[row][col]
            r = int((float(temp[0]) * 0.393) + (float(temp[1]) * 0.769) + (float(temp[2]) * 0.189))

            if r > 255:
                r = 255
            g = int((float(temp[0]) * 0.349) + (float(temp[1]) * 0.686) + (float(temp[2] * 0.168)))
            if g > 255:
                g = 255

            b = int((float(temp[0]) * 0.272) + (float(temp[1]) * 0.534) + (float(temp[2]) * 0.131))
            if b > 255:
                b = 255

            image_matrix[row][col][0] = r
            image_matrix[row][col][1] = g
            image_matrix[row][col][2] = b

    return image_matrix
    # result_matrix = sepia(image_matrix)
    # image_io.write_to_file('outputs/sepia.png', result_matrix)


def blur(image_matrix):
    output = copy.deepcopy(image_matrix)
    for row in range(len(output)):
        for col in range(len(output[row])):
            neighbors = []
            red_temp = []
            green_temp = []
            blue_temp = []

            top_left = (row - 1, col - 1)
            top = (row - 1, col)
            top_right = (row - 1, col + 1)
            left = (row, col - 1)
            center = (row, col)
            right = (row, col + 1)
            bottom_left = (row + 1, col - 1)
            bottom = (row + 1, col)
            bottom_right = (row + 1, col + 1)

            positions = [top_left, top, top_right, left, center, right, bottom_left, bottom, bottom_right]
            for i in positions:
                if ((i[0] >= 0 and i[0] < len(output)) and (i[1] >= 0 and i[1] < len(output[row]))):
                    red_temp.append(output[i[0]][i[1]][0])
                    green_temp.append(output[i[0]][i[1]][1])
                    blue_temp.append(output[i[0]][i[1]][2])
                    red_avg = sum(red_temp) // len(red_temp)
                    green_avg = sum(green_temp) // len(green_temp)
                    blue_avg = sum(blue_temp) // len(blue_temp)
                    image_matrix[row][col][0] = red_avg
                    image_matrix[row][col][1] = green_avg
                    image_matrix[row][col][2] = blue_avg
    return image_matrix


def threshold(image_matrix,red_threshold=(0, 255),
green_threshold=(0, 255),blue_threshold=(0, 255)):
  red_low = red_threshold[0]
  red_high = red_threshold[-1]
  green_low = green_threshold[0]
  green_high = green_threshold[-1]
  blue_low = blue_threshold[0]
  blue_high = blue_threshold[-1]
  for row in image_matrix:
    for col in row:
      if col[0] not in range(red_low,red_high + 1):
        col[0] = 0
        col[1] = 0
        col[2] = 0
      if col[1] not in range(green_low,green_high + 1):
        col[0] = 0
        col[1] = 0
        col[2] = 0
      if col[2] not in range(blue_low,blue_high + 1):
        col[0] = 0
        col[1] = 0
        col[2] = 0
  return image_matrix