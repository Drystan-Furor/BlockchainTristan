[Writing e2e tests in Postman](https://learning.postman.com/docs/writing-scripts/test-scripts/ "Writing e2e tests")

# Writing tests
Tests confirm that your API is working as expected, that integrations between services are functioning reliably, and that any changes haven't broken existing functionality. You can write test scripts for your Postman API requests in JavaScript. You can also use test code to aid the debugging process when something goes wrong with your API project. For example, you might write a test to validate your API's error handling by sending a request with incomplete data or wrong parameters.

### Contents
- Adding tests
- Adding tests to gRPC requests
- Writing test scripts
- Validating responses
- Formatting test result messages with pm.expect
- Using snippets
- Testing collections and folders
- Debugging your steps

---

## Adding tests
> You can add tests to individual requests, collections, and folders in a collection. Postman includes code snippets you add and then change to suit your test logic.

To add tests to a request, open the request and enter your code in the Tests tab. Tests will execute after the request runs. The output is in the response's Test Results tab.

![Request Test Tab](https://assets.postman.com/postman-docs/request-test-tab-v9.jpg)

## Adding tests to gRPC requests
To add tests to gRPC requests:

Go to the Scripts tab in your gRPC request.
Select the execution hook (Before invoke or After response) to which you want to add a test.
Use snippets from the right panel to add a test or write customized assertion.
Both the execution hooks are available for all gRPC requests regardless of the method type being unary, client streaming, server streaming, or bidirectional streaming. Your scripts can include however many tests you need and will save along with the rest of your request when you select Save.

> Tests are run when you select Invoke, either before or after the request is invoked. If you select Cancel, the request execution and any further script execution.

If there are any errors in your Before invoke script, it will stop the request execution.

## Writing test scripts
Test scripts can use dynamic variables, carry out test assertions on response data, and pass data between requests. In the Tests tab for a request, enter your JavaScript manually or select Snippets next to the code editor.

Tests execute after the response is received. When you select Send, Postman runs your test script after the response data returns from the API.

If you need to execute code before a request runs, use Pre-request Scripts instead. See Intro to scripts for more on the how your scripts execute when your requests run.

## Validating responses
To validate the data returned by a request, you can use the pm.response object in a test. Define tests using the pm.test function, providing a name and function that returns a boolean (true or false) value indicating if the test passed or failed. Use ChaiJS BDD syntax and pm.expect in your assertions to test the response detail.

The first parameter for the .test function is a text string that will appear in the test result output. Use this to identify your tests, and communicate the purpose of a test to anyone viewing the results.

For example, enter the following in the Tests tab of a request to test if the response status code is 200:
```
pm.test("Status test", function () {
pm.response.to.have.status(200);
});
```
Select Send to run your request and open Test Results in the response section. The tab header displays how many tests passed and how many ran in total. You can also view the number of Passed, Skipped, and Failed test results.

If the request returned a 200 status code, the test passes. To find out what happens with a different status code, change the expected status code in your test script and run the request again.

## Formatting test result messages with pm.expect
Using the pm.expect syntax gives your test result messages a different format. Experiment with the alternatives to achieve the output you find most useful.

> Use the Run in Postman button in the Intro to writing tests collection to import templates containing some example test scripts into Postman and experiment with the code.

Your code can test the request environment, as in the following example:
```
pm.test("environment to be production", function () {
pm.expect(pm.environment.get("env")).to.equal("production");
});
```
You can use different syntax variants to write your tests in a way that you find readable, and that suits your application and testing logic.
```
pm.test("response should be okay to process", function () {
pm.response.to.not.be.error;
pm.response.to.have.jsonBody("");
pm.response.to.not.have.jsonBody("error");
});
```
Your tests can establish validity of request responses using syntax that you tailor to the response data format.
```
pm.test("response must be valid and have a body", function () {
pm.response.to.be.ok;
pm.response.to.be.withBody;
pm.response.to.be.json;
});
```
Your scripts can include however many tests you need and will save along with the rest of your request detail when you select Save. If you share a collection, publish documentation, or use the Run in Postman button, your test code will be included for anyone who views or imports your templates.

## Using snippets
You can use a curated list of commonly-used test code snippets to write your tests. Snippets are available in the right panel of the script editor. Selecting a snippet adds the required code automatically to your script, helping you get started quickly with your testing. Once added to your script, you can edit the snippets to meet your specific testing requirements.

## Testing collections and folders
You can add test scripts to a collection, a folder, or a single request within a collection. A test script associated with a collection will run after every request in the collection. A test script associated with a folder will run after every direct child request in the folder. This enables you to reuse commonly executed tests after requests. The execution order for each request will be collection tests, folder tests and then request tests.

> Adding scripts to collections and folders enables you to test the workflows in your API project. This helps to ensure that your requests cover typical scenarios, providing a reliable experience for application users.

You can update collection and folder scripts by selecting the view more actions icon More actions icon next to the collection or folder name, and selecting Edit. Choose the Tests tab to add or update your script. You can also add collection scripts when you first create a collection.

When you run a collection the collection runner displays the test results, including the response time in milliseconds and details about whether a specific request in the collection passed or failed its tests.

![Collection Tests](https://assets.postman.com/postman-docs/collection-tests-run-v9.jpg)

You can write scripts to control the order in which your requests run using branching and looping.

## Debugging your tests
If you are having trouble with your tests:

Check if there are any errors in your scripts. A red badge will highlight scripts with errors. You can also check the response section for specific errors.
Debug your tests using the log statements to ensure that you are asserting on correct data.



```
{
  "author": "Tristan",
  "email": "artstristan@gmail.com",
}
```