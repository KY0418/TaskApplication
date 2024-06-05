const TaskData = {
  title:"test",
  year:2024,
  month:6,
  day:6,
  staff_id:"000003",
  category:"仕事",
  priority_id:2,
  status_id:"2"
}

describe('move TaskAdd', () => {
  it('PostData',()=>{
    const {title,year,month,day,staff_id,category,priority_id,status_id} = TaskData
    cy.visit('localhost:3000/App/TaskAdd')
    cy.get('input[data-cy="title"]').type(title)
    cy.get('select[data-cy="date"]').select(5)
    cy.get('select[data-cy="mdate"]').select(5)
    cy.get('select[data-cy="ddate"]').select(5)
    cy.get('select[data-cy="staff"]').select(staff_id)
    cy.get('select[data-cy="category"]').select(category)
    cy.get('select[data-cy="importance"]').select(priority_id)
    cy.get('[type="radio"]').check(status_id)
  })
})
