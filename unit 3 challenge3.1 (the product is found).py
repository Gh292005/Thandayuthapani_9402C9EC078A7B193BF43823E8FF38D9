def linearSearchProduct(productList,targetProduct):
    indices=[]

    for index,product in enumerate(productList):
        if product==targetProduct:
            indices.append(index)

    return indices



protucts=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
result=linearSearchProduct(protucts,target)
print(result)



