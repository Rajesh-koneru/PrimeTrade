import { createContext, useState } from "react";
import initialProducts from "../data/products";

export const ProductContext = createContext();

export const ProductProvider = ({ children }) => {
  const [products, setProducts] = useState(initialProducts);

  const addProduct = (product) => {
    setProducts([...products, { ...product, id: Date.now() }]);
  };

  const deleteProduct = (id) => {
    setProducts(products.filter((p) => p.id !== id));
  };

  const updateProduct = (updatedProduct) => {
    setProducts(
      products.map((p) =>
        p.id === updatedProduct.id ? updatedProduct : p
      )
    );
  };

  return (
    <ProductContext.Provider
      value={{ products, addProduct, deleteProduct, updateProduct }}
    >
      {children}
    </ProductContext.Provider>
  );
};