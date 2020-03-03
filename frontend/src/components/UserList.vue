<template>
  <div class="container">
    <div v-for="user in this.users" v-bind:key="user.id">
      <p>{{ user.username }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      users: []
    };
  },
  async mounted() {
    try {
      var result = await axios({
        method: "POST",
        url: "http://127.0.0.1:8000/graphql/",
        data: {
          query: `
			{
                users{
                    id
                    username
                    email
                    firstName
                    lastName
                }
            }
			`
        }
      });
      this.users = result.data.data.users;
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style></style>
