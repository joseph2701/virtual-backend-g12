import {Router} from "express";
import {
    crearProducto,    
    listarProductos,
    actualizarProductos,
    eliminarProductos,
} from "../controllers/productos.controller.js";

import {validarAdmin,verificarToken} from "../utils/validador.js"

export const productosRouter=Router();

productosRouter
    .route("/Productos")
    .post(verificarToken,validarAdmin,crearProducto)
    .get(listarProductos);

productosRouter
    .route("/Producto/:id")
    //el all sirve para indiicar de forma general,  las middleware que tendran que llamarse antes del PUT y DELETE
    .all(verificarToken,validarAdmin)
    .put(actualizarProductos)
    .delete(eliminarProductos);

