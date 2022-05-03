import {Router} from "express";
import {crearDetallePedido} from "../controllers/detallePedido.controller.js";
import { verificarToken,validarCliente } from "../utils/validador.js";
export const detallePedidoRouter=Router();

detallePedidoRouter.post(
    "/detalle-pedido",
    verificarToken,
    validarCliente,
    crearDetallePedido
);

