import {Router} from "express";
import {crearUsuario,login} from "../controllers/usuarios.controller.js";

export const usuariosRouter=Router();
usuariosRouter.route("/Registro").post(crearUsuario);
usuariosRouter.route("/login").post(login);
