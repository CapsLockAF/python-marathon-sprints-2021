const product = function() {
    return [].reduce.call(arguments, function(res, elem) {
      return res * elem;
    }, this.product);
};

const contextObj = {
  product: 10 
}

const getProduct = (x, y) => product.call(contextObj, 2, 3, x, y)


