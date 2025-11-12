import { useEffect, useState } from 'react';
import { Flatlist, Text, View } from 'react-native';

const LOCAL_DATA = [
  {id: "1", title: "Item 1", description: "Descrição do Item 1"},
  {id: "2", title: "Item 2", description: "Descrição do Item 2"},
  {id: "3", title: "Item 3", description: "Descrição do Item 3"},
  {id: "4", title: "Item 4", description: "Descrição do Item 4"},
  {id: "5", title: "Item 5", description: "Descrição do Item 5"},
  {id: "6", title: "Item 6", description: "Descrição do Item 6"},
  {id: "7", title: "Item 7", description: "Descrição do Item 7"},
  {id: "8", title: "Item 8", description: "Descrição do Item 8"},
  {id: "9", title: "Item 9", description: "Descrição do Item 9"},
];

const API_URL = "https://jsonplaceholder.typicode.com/photos?_limit=1000";

export default function App() {

  const [data, setData] = useState([]);
  useEffect(() => {
    fetch(API_URL)
      .then((response)=>response.json())
      .then((json) => setData(json))
      .catch((error) => console.error())
  }, []);

  const render = ({item}) => (
    <View>
      <View>
        <Text>{item.title}</Text>
        <Text>{item.url}</Text>
      </View>
      <Button title="Adicionar Item" color="#1d1d1d" />
    </View>
  );

  return (
    <Flatlist
    // Ddados da lista 
      data={LOCAL_DATA}
      // Renderiza cada item da lista
      renderItem={render}
      // Para identificar cada elemento
      keyExtractor={(item) => item.id}
    />
  );
}