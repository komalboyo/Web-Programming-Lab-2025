let employees = []; // Simulating an in-memory database.

function displayEmployees() {
    const tableBody = document.getElementById('employeeTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';

    employees.forEach((employee, index) => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${employee.name}</td>
            <td>${employee.position}</td>
            <td>${employee.salary}</td>
            <td>
                <button onclick="editEmployee(${index})">Edit</button>
                <button class="delete" onclick="deleteEmployee(${index})">Delete</button>
            </td>
        `;
    });
}

function addOrUpdateEmployee() {
    const employeeName = document.getElementById('employeeName').value;
    const employeePosition = document.getElementById('employeePosition').value;
    const employeeSalary = document.getElementById('employeeSalary').value;
    const employeeId = document.getElementById('employeeId').value;

    const employee = {
        name: employeeName,
        position: employeePosition,
        salary: parseFloat(employeeSalary)
    };

    if (employeeId) {
        employees[employeeId] = employee; // Update existing employee
    } else {
        employees.push(employee); // Add new employee
    }

    resetForm();
    displayEmployees();
}

function editEmployee(index) {
    const employee = employees[index];
    document.getElementById('employeeName').value = employee.name;
    document.getElementById('employeePosition').value = employee.position;
    document.getElementById('employeeSalary').value = employee.salary;
    document.getElementById('employeeId').value = index;
}

function deleteEmployee(index) {
    employees.splice(index, 1);
    displayEmployees();
}

function resetForm() {
    document.getElementById('employeeForm').reset();
    document.getElementById('employeeId').value = '';
}

displayEmployees();
