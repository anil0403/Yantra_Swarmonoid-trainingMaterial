from Grid import generate_matrix_from_image
import cv2
import numpy as np

# how it sees and processes image
image_path = '\Yantra_Swarmonoid-trainingMaterial\images\TestGround.png'

line_color = (255, 0, 0)
line_thickness = 1  
grid_spacing = 50 
frame = cv2.imread(image_path)

if frame is None:
    print("Error: Image not found or unable to load.")
    exit(0)

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
arucoParams = cv2.aruco.DetectorParameters_create()

(corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

if ids is not None:
    for i, marker_id in enumerate(ids.flatten()):
        corners_array = corners[i][0]
        if len(corners_array) > 0:
            corner_tuples = np.array(corners_array, dtype=np.int32)
            cv2.polylines(frame, [np.array(corner_tuples)], True, (0, 255, 0), 2)

            centroid = np.mean(corners_array, axis=0, dtype=np.int32)
            cv2.putText(frame, f"ID: {marker_id}", tuple(centroid), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Vertical lines
for x in range(grid_spacing, frame.shape[1], grid_spacing):
    cv2.line(frame, (x, 0), (x, frame.shape[0]), line_color, line_thickness)

# Horizontal lines
for y in range(grid_spacing, frame.shape[0], grid_spacing):
    cv2.line(frame, (0, y), (frame.shape[1], y), line_color, line_thickness)

cv2.imwrite('images\BoardGrid.png',frame)
cv2.imshow('Grid From Board',frame)
print(generate_matrix_from_image(frame))

cv2.waitKey(0)
cv2.destroyAllWindows()