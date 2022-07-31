<template>
  <div id="app">
    
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-6 mx-2" placeholder="Nombre" v-model="producto.nombre">
        <input type="text" class="form-control col-6 mx-2" placeholder="Precio" v-model="producto.precio">
        <input type="text" class="form-control col-6 mx-2" placeholder="Stock" v-model="producto.stock">
        <input type="text" class="form-control col-6 mx-2" placeholder="Medidas" v-model="producto.medidas">
        <input type="text" class="form-control col-6 mx-2" placeholder="Colores" v-model="producto.colores">
        <!-- <input type="text" class="form-control col-3 mx-2" placeholder="Foto">-->
        <button class="btn btn-success">Ingresar</button>
      </div>
    </form>
      

    <table class="table">
      <thead>
        <th>id</th>
        <th>Nombre</th>
        <th>Precio</th>
        <th>Stock</th>
        <th>Medidas</th>
        <th>Colores</th>
        <th>Foto</th>
      </thead>
      <tbody>
        <tr v-for="producto in Producto" :key="producto.id" @dblclick="$data.producto = producto">
          <td>{{ producto.id }}</td>
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.precio }}</td>
          <td>{{ producto.stock }}</td>
          <td>{{ producto.medidas }}</td>
          <td>{{ producto.colores }}</td>
          <td>{{ producto.foto }}</td>
          <!-- <td><img src="{{ producto.foto }}"></td> -->
          <td>
            <button class="btn btn-outline-danger-btn-sm mx-1" @click="deleteProducto(producto)">x</button>
          </td>
          <!-- <td>{{ productos.foto }}</td> -->
        </tr>
      </tbody>
    </table>
    
  </div>

</template>

<script>

// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // }
  data(){
    return {
      
      producto: {},

      Producto: [],

    }
  },

  async created(){
    await this.getProductos();
  },

  methods:{
    
    submitForm(){

      if(this.producto.id === undefined){
          this.createProducto();
      } else {
          this.editProducto();
      }

    },

    async getProductos(){
      var response = await fetch('http://127.0.0.1:8000/api/catalogo/');
      this.Producto = await response.json();
    },

    async createProducto(){

      await this.getProductos();

      await fetch('http://127.0.0.1:8000/api/catalogo/' ,{
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.producto)
      });

      await this.getProductos();
      
    },

    async editProducto(){
      await this.getProductos();

      await fetch("http://127.0.0.1:8000/api/catalogo/"+this.producto.id+"/" ,{
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.producto)
      });

      await this.getProductos();

      this.producto = {};

    },

    async deleteProducto(producto){
      await this.getProductos();
      
      var id = producto.id

      await fetch("http://127.0.0.1:8000/api/catalogo/"+id+"/" ,{
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.producto)
      });

      await this.getProductos();
    },
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
