in this file og google colab i am answering these questions:

Q1 : . Generate a simple example of a matrix X of dimensions 2 × 50 for which calculating the SVD
of X is not equivalent to calculating the principle components of X. Use a scatter plot to show
the points (the columns of X) on a 2D plain. On the same plot, use arrows (pyplot.arrow) to
show the direction of the leading principle component and the leading left singular vector.

Q2 : Coding problem: For the image in (circle.png), extract all overlapping patches of size 5 × 5
(for example using Matlab’s im2col function or feature extraction.image.extract patches 2d in
Python’s scikit-learn). Reshape each patch into a 25 size vector, and concatenate all patches
to obtain the matrix of patch set.
Calculate PCA of the resulting patch set. The leading principle components of this patch
set are vectors of size 25. For the 3 leading principle components, reshape each back into an
image of size 5 × 5 and generate a figure by imshow. Try to explain the images observed.

Q3:  Compression. Load the file numbers.mat. The variable ‘mat’ is an image. Treat this image
as a data matrix Xd and apply SVD to it.
• Reconstruct the matrix Xˆd and plot it as a grayscale image using d = 1, 10, 20, 100
principal components .
• Calculate the reconstruction error.
• Calculate the compression rate (using Ud, Sd, Vd instead of X).

Q4:  Search the Kaggle database for a data of your preference and download it. Process the data
by computing the leading principle components. Create a scatter plot with 2 of the PCA
coordinates