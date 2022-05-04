export async function getArticles(text) {
  const response = await fetch("http://localhost:5000/articles", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(text),
  });
  const data = await response.json();
  return data;
}

export default getArticles;
