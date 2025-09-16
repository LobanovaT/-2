//Список
ArrayList<String> arrayList = new ArrayList<>(128)
//Стек
Stack<String> stack = new Stack<String>();  
stack.push("Математика");  
stack.push("Русский");  
stack.push("ИКТ");  
String element = stack.pop();  
System.out.println("Removed Element: " + element);  
