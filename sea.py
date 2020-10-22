import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
print(iris.head())
print(iris.shape)
print(iris.describe())
print(sns.jointplot(x="sepal_length", y="sepal_width",data=iris))
plt.show()
print(sns.pairplot(iris))
plt.show(0)