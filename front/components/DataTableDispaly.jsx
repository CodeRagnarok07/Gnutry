import React from 'react'

export default function DataTableDispaly({ data }) {

  const th = Object.keys(data[0])


  const render_td =(value,index)=>{
    return  <td key={index} > {value} </td>
  }

  const render_tr =(value,index)=>{
    return  <td key={index} > {value} </td>
  }

  return ( data &&
    <table>

      <thead>
        <tr>
          {th.map((value, index) => (
            <th className='capitalize' key={index}>
              <div className="">
                {render_td(value, index)}
              </div>
            </th>
          ))}
        </tr>
      </thead>

      <tbody>
        {data.map((e, i) => (
          <tr key={i}>
            {Object.entries(e).map((value, index) => (
             render_tr(value,index)
            ))}


          </tr>
        ))}
      </tbody>

    </table>
  )
}
