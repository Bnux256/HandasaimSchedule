<script>
	let classes = [];
	const url = "http://localhost:8000/?getClasses=true";
	fetch(url).then((response) => {
      return response.json();
    }).then((data) => {
    console.log(data);
		classes = data;
    })
</script>

<h1>Hello {name}!</h1>
{#each classes as cur_class}
<a target="_blank" href="http://localhost:8000/?class={cur_class}">{cur_class}</a>
<br>
{/each}
