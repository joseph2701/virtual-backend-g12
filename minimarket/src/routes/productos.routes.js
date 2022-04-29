import {Router} from "express";
import {
    crearProducto,    
    listarProductos,
    actualizarProductos,
    eliminarProductos,
} from "../controllers/productos.controller.js";

export const productosRouter=Router();
productosRouter.route("/Productos").post(crearProducto).get(listarProductos);
productosRouter.route("/Producto/:id").put(actualizarProductos).delete(eliminarProductos);