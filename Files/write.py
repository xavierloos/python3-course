# 1.Create a file object for the file bad_bands.txt using the open() function with the w argument. Assign this object to the temporary variable bad_bands_doc.

# 2.Use the bad_bands_doc.write() method to add the name of a musical group you dislike to the document bad_bands.

with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("One Direction")