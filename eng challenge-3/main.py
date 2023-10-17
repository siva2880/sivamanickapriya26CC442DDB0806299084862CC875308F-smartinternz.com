def linearSearchProduct(productList,targetProduct):
indices=[]
For index,product in enumerate(productList):
if product==targetProduct:
Indices.append(index)
Return indices
#Example usage:
Products=["shoes","boot","loafer","shoes","sandals","shoes"]
Target="shoes"
Result=linearSearchProduct(products,target)
Print(result)