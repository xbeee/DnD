import React from "react";

// Определяем тип значения, предоставляемого контекстом
interface AppContextType {
	token: string | null;
	setAuthToken: (newToken: string | null) => void;
}

// Создаем контекст с указанием типа значения
const AppContext = React.createContext<AppContextType | undefined>(undefined);

export default AppContext;
