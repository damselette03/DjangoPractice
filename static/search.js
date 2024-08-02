const SearchRestaurant = () => {
    console.log("找餐廳");
    const Input = document.getElementById('RestaurantInput');
    const text = Input.value;

    const query = `
        query {
            foodsByRestaurantName(restaurantName: "${text}"){
                id
                name
                price
            }
        }`;
    
    fetch('/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
    })
    .then(response => response.json())
    .then(data => {
        // 提取返回的数据
        const foods = data.data.foodsByRestaurantName;
        const liNode = document.getElementById('RestaurantInfo');
        liNode.innerHTML = '';
        // 清空之前的内容
        
        if (!foods || foods.length === 0) {
            const noResultsMessage = document.createElement('p');
            noResultsMessage.textContent = '未找到符合条件的食物。';
            liNode.appendChild(noResultsMessage);
        }else{
            const pNode = document.createElement('p');
            pNode.innerHTML = `餐廳名稱: ${text}`;
            liNode.appendChild(pNode);
        }
        // 遍历数据并处理
        foods.forEach(food => {
            console.log(`ID: ${food.id}`);
            console.log(`Name: ${food.name}`);
            console.log(`Price: ${food.price}`);
            const divNode = document.createElement('div');
                divNode.innerHTML = `
                    <p>名字: ${food.name}</p>
                    <p>價格: ${food.price}</p>
                `;
                liNode.appendChild(divNode);
        });
    })
    .catch(error => {
      console.error('Error:', error);
    });

    document.getElementById('RestaurantInput').innerHTML = '';  // 清空結果
}

document.getElementById('RestaurantSearcher').addEventListener("click", SearchRestaurant);