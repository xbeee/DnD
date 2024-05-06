import React from "react";
import Profile from "../components/Profile";
import axios from "axios";
import { Navigate } from "react-router-dom";

export default function User() {
	async function logMeOut() {
		try {
			await axios.post("http://127.0.0.1:5000/logout");
			localStorage.removeItem("name");
			localStorage.removeItem("token");
			window.location.href = "/";
		} catch (error) {
			alert("Ошибка при выходе из аккаунта, повторите попытку");
			console.log(error.response);
		}
	}

	return (
		<div>
			<Profile />
			<button onClick={logMeOut}>Выйти</button>
		</div>
	);
}
