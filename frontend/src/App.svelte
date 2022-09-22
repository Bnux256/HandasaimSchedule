<script>

	// get list of classes
	let classes = [];
	const url = "http://localhost:8000/?getClasses=true";
	fetch(url).then((response) => {
		return response.json();
	}).then((data) => {
	console.log(data);
		classes = data;
})

	let schedule = [];
	function get_schedule(chosen_class) {
		const url = `http://localhost:8000/?class=${chosen_class}`;
		fetch(url).then((response) => {
		return response.json();
		}).then((data) => {
			console.log(data);
			schedule = data;
		})
		console.log(schedule)
	}
</script>

<main>
	<h1>מערכת שעות יומית - תיכון הנדסאים</h1>
	<h4>לקוח לא רשמי למערכת של תיכון הנדסאים הרצליה.</h4>
	<br>

	{#each classes as cur_class}
	<!-- <a target="_blank" href="http://localhost:8000/?class={cur_class}">{cur_class}</a> -->
	<button on:click={get_schedule(cur_class)}>
		{cur_class}
	</button>
	{/each}	

	
	<!-- print schedule -->
	<table class="center">
		{#each schedule as [i, lesson]}
			<tr>
				<th>{i}</th>
				{#if lesson!==null}
				<th>{lesson}</th>
				{/if}
			</tr>
		{/each}
	</table>
	
	<footer>
		<p><a href="https://github.com/Bnux256/HandasaimSchedule">אודות הפרויקט</a></p>
		<p><a href="https://handasaim.co.il/2020/07/16/%d7%9e%d7%a2%d7%a8%d7%9b%d7%aa-%d7%99%d7%95%d7%9e%d7%99%d7%aa/">קישור למערכת המקורית</a></p>
	</footer>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #8400ff;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	.center {
  		margin-left: auto;
  		margin-right: auto;
	}
</style>