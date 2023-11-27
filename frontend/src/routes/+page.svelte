<script>
	import { Button, GradientButton, Input, Toast } from 'flowbite-svelte';
	import { CheckCircleSolid } from 'flowbite-svelte-icons';

	let baseAPIURL = 'https://url-shortener-ag.up.railway.app';
	var longURL = '';
	$: shortURL = null;
	$: showToast = false;
	$: buttonDisabled = longURL.trim().length <= 5;

	async function getShortURL() {
		showToast = false;

		if (longURL.length > 0) {
			// Send API request
			var response = await fetch(`${baseAPIURL}/url`, {
				method: 'POST',
				body: JSON.stringify({ url: longURL }),
				headers: { 'Content-type': 'application/json; charset=UTF-8' }
			});

			if (response.status == 201) {
				var json_data = await response.json();
				shortURL = json_data.url;
				showToast = true;
			}
		}
	}

	function copyLinkToClipboard() {
		navigator.clipboard.writeText(shortURL);
	}
</script>

{#if showToast}
	<Toast
		color="green"
		dismissable={true}
		position="top-right"
		divClass="w-full max-w-md p-4 text-white bg-green-500 shadow gap-3"
		contentClass="w-full text-lg font-normal"
	>
		<svelte:fragment slot="icon">
			<CheckCircleSolid class="w-5 h-5" />
			<span class="sr-only">Check icon</span>
		</svelte:fragment>
		URL shortened successfully!
	</Toast>
{/if}

<!-- Page Container -->
<div id="page-container" class="mx-auto flex min-h-screen w-full min-w-[320px] flex-col">
	<!-- Page Content -->
	<main id="page-content" class="flex max-w-full flex-auto flex-col">
		<!-- Page Section -->
		<div class="mx-auto w-1/3 max-w-10xl p-4 lg:p-8">
			<div class="flex items-center justify-center pt-32">
				<Input
					bind:value={longURL}
					size="lg"
					type="text"
					id="long-url"
					placeholder="https://www.google.com"
					required
				/>
			</div>
			<div class="flex items-center justify-center pt-8">
				<GradientButton
					disabled={buttonDisabled}
					on:click={getShortURL}
					color="greenToBlue"
					size="lg"
					shadow="true">Shorten</GradientButton
				>
			</div>
			{#if shortURL}
				<div class="flex items-center justify-start pt-16">
					<Input bind:value={shortURL} class="w-3/4 mr-8" size="lg" type="text" readonly />
					<Button on:click={copyLinkToClipboard} size="lg">Copy URL</Button>
				</div>
			{/if}
		</div>
		<!-- END Page Section -->
	</main>
	<!-- END Page Content -->
</div>
<!-- END Page Container -->
