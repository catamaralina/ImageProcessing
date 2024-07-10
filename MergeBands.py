# Merge Bands
# Tali JOnker
# 2024-06-28

# Function:
# Merges individual TIF bands into one raster.

import arcpy

arcpy.env.workspace=r"C:\Users\talij\Documents\_CODINGPROJECTS\imagery"
# arcpy.CompositeBands_management("b1.TIF;b2.TIF;b3.TIF;b4.TIF;b5.TIF;b6.TIF;b7.TIF;b8.TIF;b9.TIF;b10.TIF;b11.TIF", "2022_10_22.TIF")
arcpy.CompositeBands_management("blue_b2.TIF;green_b3.TIF;red_b4.TIF;b5.TIF;b6.TIF;b7.TIF", "2022_10_22_b2-7.TIF")
print("Merge Complete")